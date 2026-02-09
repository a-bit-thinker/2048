#!/usr/bin/env python3
"""Terminal 2048 game using curses."""

import argparse
import ctypes
import curses
import math
import multiprocessing as mp
import os
import random
import sys
import time
from contextlib import contextmanager
from typing import Dict, List, Optional, Tuple

SIZE = 4
TARGET = 2048
SPAWN_FOUR_CHANCE = 0.1
AUTO_DEFAULT_SPEED = 2.0
BOT_DIRECTIONS = ("up", "left", "right", "down")
MAX_CHANCE_BRANCHES = 8
AUTO_MOVE_TIME_BUDGET = 0.28
AUTO_MOVE_MAX_THINK_TIME = 1.0
NNEONNEO_STARTUP_TIMEOUT = 1.5

Board = List[List[int]]
NNEONNEO_MOVE_TO_DIR = {0: "up", 1: "down", 2: "left", 3: "right"}


class SearchTimeout(Exception):
    """Raised when autoplay search exceeds the move time budget."""


def board_to_nibble64(board: Board) -> int:
    packed = 0
    shift = 0
    for r in range(SIZE):
        for c in range(SIZE):
            value = board[r][c]
            rank = min(15, int(math.log2(value))) if value else 0
            packed |= (rank & 0xF) << shift
            shift += 4
    return packed


@contextmanager
def suppress_native_stdout() -> "ctypes.CDLL":
    libc = ctypes.CDLL(None)
    libc.fflush(None)
    devnull_fd = os.open(os.devnull, os.O_WRONLY)
    stdout_fd = 1
    saved_fd = os.dup(stdout_fd)
    os.dup2(devnull_fd, stdout_fd)
    try:
        yield
    finally:
        libc.fflush(None)
        os.dup2(saved_fd, stdout_fd)
        os.close(saved_fd)
        os.close(devnull_fd)


class NneonneoEngine:
    def __init__(self, lib_path: str):
        self.lib = ctypes.CDLL(lib_path)
        self.lib.init_tables.argtypes = []
        self.lib.init_tables.restype = None
        self.lib.find_best_move.argtypes = [ctypes.c_uint64]
        self.lib.find_best_move.restype = ctypes.c_int
        self.lib.init_tables()

    def choose_move(self, board: Board) -> Optional[str]:
        packed = board_to_nibble64(board)
        with suppress_native_stdout():
            move = self.lib.find_best_move(ctypes.c_uint64(packed))
        return NNEONNEO_MOVE_TO_DIR.get(move)


def _nneonneo_worker(conn, lib_path: str) -> None:
    try:
        engine = NneonneoEngine(lib_path)
        conn.send(("ready", ""))
    except Exception as exc:
        try:
            conn.send(("error", str(exc)))
        finally:
            conn.close()
        return

    while True:
        try:
            command, payload = conn.recv()
        except (EOFError, OSError):
            break

        if command == "stop":
            break
        if command != "move":
            continue

        try:
            with suppress_native_stdout():
                move = engine.lib.find_best_move(ctypes.c_uint64(payload))
            conn.send(("move", int(move)))
        except Exception as exc:
            try:
                conn.send(("error", str(exc)))
            finally:
                break

    conn.close()


class TimedNneonneoEngine:
    def __init__(self, lib_path: str, move_timeout: float):
        self.lib_path = lib_path
        self.move_timeout = max(0.05, move_timeout)
        self._process: Optional[mp.Process] = None
        self._conn = None
        self.last_error: Optional[str] = None

    @staticmethod
    def _stop_process(process: Optional[mp.Process]) -> None:
        if process is None:
            return
        if process.is_alive():
            process.terminate()
            if process.is_alive() and hasattr(process, "kill"):
                process.kill()
        try:
            process.join(timeout=0.0)
        except (ValueError, OSError):
            pass

    def _clear_worker(self) -> None:
        if self._conn is not None:
            try:
                self._conn.close()
            except OSError:
                pass
            self._conn = None
        if self._process is not None:
            self._stop_process(self._process)
            self._process = None

    def close(self) -> None:
        if self._conn is not None:
            try:
                self._conn.send(("stop", 0))
            except OSError:
                pass
        self._clear_worker()

    def _ensure_worker(self, startup_timeout: Optional[float] = None) -> bool:
        if self._conn is not None and self._process is not None and self._process.is_alive():
            return True

        self._clear_worker()
        parent_conn, child_conn = mp.Pipe(duplex=True)
        process = mp.Process(target=_nneonneo_worker, args=(child_conn, self.lib_path), daemon=True)
        process.start()
        child_conn.close()

        wait_startup = NNEONNEO_STARTUP_TIMEOUT if startup_timeout is None else max(0.05, startup_timeout)
        if not parent_conn.poll(wait_startup):
            self.last_error = "nneonneo worker startup timed out"
            try:
                parent_conn.close()
            except OSError:
                pass
            self._stop_process(process)
            return False

        try:
            kind, payload = parent_conn.recv()
        except (EOFError, OSError):
            kind, payload = "error", "nneonneo worker exited during startup"

        if kind != "ready":
            self.last_error = str(payload) if payload else "failed to initialize nneonneo worker"
            try:
                parent_conn.close()
            except OSError:
                pass
            self._stop_process(process)
            return False

        self._conn = parent_conn
        self._process = process
        self.last_error = None
        return True

    def warmup(self) -> bool:
        return self._ensure_worker()

    def choose_move(self, board: Board, timeout: Optional[float] = None) -> Optional[str]:
        total_budget = max(0.05, self.move_timeout if timeout is None else timeout)
        started_at = time.monotonic()

        if not self._ensure_worker(startup_timeout=total_budget):
            return None

        packed = board_to_nibble64(board)
        elapsed = time.monotonic() - started_at
        remaining = total_budget - elapsed
        if remaining <= 0:
            self.last_error = f"nneonneo timed out after {total_budget:.2f}s"
            return None
        wait_seconds = max(0.05, remaining)

        try:
            self._conn.send(("move", packed))
        except OSError:
            self.last_error = "nneonneo worker send failed"
            self._clear_worker()
            return None

        if not self._conn.poll(wait_seconds):
            self.last_error = f"nneonneo timed out after {wait_seconds:.2f}s"
            self._clear_worker()
            return None

        try:
            kind, payload = self._conn.recv()
        except (EOFError, OSError):
            self.last_error = "nneonneo worker disconnected"
            self._clear_worker()
            return None

        if kind == "move":
            return NNEONNEO_MOVE_TO_DIR.get(int(payload))

        self.last_error = str(payload) if payload else "nneonneo worker returned an error"
        self._clear_worker()
        return None


def load_nneonneo_engine(move_timeout: float) -> Tuple[Optional[TimedNneonneoEngine], Optional[str]]:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    lib_path = os.path.join(base_dir, "2048-ai", "bin", "2048.so")
    if not os.path.isfile(lib_path):
        return None, f"missing shared library: {lib_path}"
    try:
        engine = TimedNneonneoEngine(lib_path, move_timeout=move_timeout)
        if not engine.warmup():
            err = engine.last_error or "failed to start nneonneo worker"
            engine.close()
            return None, err
        return engine, None
    except Exception as exc:
        return None, str(exc)


def rotate_matrix_clockwise(matrix: List[List[float]]) -> List[List[float]]:
    size = len(matrix)
    return [[matrix[size - 1 - r][c] for r in range(size)] for c in range(size)]


def flip_matrix_horizontal(matrix: List[List[float]]) -> List[List[float]]:
    return [list(reversed(row)) for row in matrix]


def build_corner_weight_matrices() -> Dict[str, List[List[float]]]:
    base = [
        [15.0, 14.0, 13.0, 12.0],
        [8.0, 9.0, 10.0, 11.0],
        [7.0, 6.0, 5.0, 4.0],
        [0.0, 1.0, 2.0, 3.0],
    ]
    top_left = base
    top_right = flip_matrix_horizontal(top_left)
    bottom_right = rotate_matrix_clockwise(rotate_matrix_clockwise(top_left))
    bottom_left = flip_matrix_horizontal(bottom_right)
    return {
        "top_left": top_left,
        "top_right": top_right,
        "bottom_right": bottom_right,
        "bottom_left": bottom_left,
    }


SNAKE_WEIGHT_BY_CORNER = build_corner_weight_matrices()


def new_board() -> Board:
    board = [[0] * SIZE for _ in range(SIZE)]
    add_random_tile(board)
    add_random_tile(board)
    return board


def add_random_tile(board: Board) -> bool:
    empty_cells = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
    if not empty_cells:
        return False
    row, col = random.choice(empty_cells)
    board[row][col] = 4 if random.random() < SPAWN_FOUR_CHANCE else 2
    return True


def slide_and_merge(line: List[int]) -> Tuple[List[int], int]:
    non_zero = [value for value in line if value != 0]
    merged: List[int] = []
    score_gain = 0

    i = 0
    while i < len(non_zero):
        if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
            value = non_zero[i] * 2
            merged.append(value)
            score_gain += value
            i += 2
        else:
            merged.append(non_zero[i])
            i += 1

    merged.extend([0] * (SIZE - len(merged)))
    return merged, score_gain


def apply_move(board: Board, direction: str) -> Tuple[Board, int, bool]:
    updated = [row[:] for row in board]
    moved = False
    score_gain = 0

    if direction in ("left", "right"):
        for r in range(SIZE):
            line = board[r][:]
            if direction == "right":
                line.reverse()

            merged, gained = slide_and_merge(line)
            if direction == "right":
                merged.reverse()

            if merged != board[r]:
                moved = True

            updated[r] = merged
            score_gain += gained
    else:
        for c in range(SIZE):
            line = [board[r][c] for r in range(SIZE)]
            if direction == "down":
                line.reverse()

            merged, gained = slide_and_merge(line)
            if direction == "down":
                merged.reverse()

            for r in range(SIZE):
                if merged[r] != board[r][c]:
                    moved = True
                updated[r][c] = merged[r]

            score_gain += gained

    return updated, score_gain, moved


def can_move(board: Board) -> bool:
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:
                return True
            if c + 1 < SIZE and board[r][c] == board[r][c + 1]:
                return True
            if r + 1 < SIZE and board[r][c] == board[r + 1][c]:
                return True
    return False


def reached_target(board: Board) -> bool:
    return any(value >= TARGET for row in board for value in row)


def evaluate_board(board: Board) -> float:
    empty_cells = 0
    merges = 0
    smoothness = 0.0
    max_tile = 0
    log_values = [[0.0] * SIZE for _ in range(SIZE)]

    for r in range(SIZE):
        for c in range(SIZE):
            value = board[r][c]
            if value == 0:
                empty_cells += 1
            else:
                log_values[r][c] = math.log2(value)
                max_tile = max(max_tile, value)

    for r in range(SIZE):
        for c in range(SIZE):
            value = board[r][c]
            if value == 0:
                continue

            if c + 1 < SIZE and board[r][c + 1] != 0:
                smoothness -= abs(log_values[r][c] - log_values[r][c + 1])
                if value == board[r][c + 1]:
                    merges += 1

            if r + 1 < SIZE and board[r + 1][c] != 0:
                smoothness -= abs(log_values[r][c] - log_values[r + 1][c])
                if value == board[r + 1][c]:
                    merges += 1

    mono_lr = mono_rl = 0.0
    mono_ud = mono_du = 0.0

    for r in range(SIZE):
        for c in range(SIZE - 1):
            left = log_values[r][c]
            right = log_values[r][c + 1]
            if left > right:
                mono_lr += left - right
            else:
                mono_rl += right - left

    for c in range(SIZE):
        for r in range(SIZE - 1):
            up = log_values[r][c]
            down = log_values[r + 1][c]
            if up > down:
                mono_ud += up - down
            else:
                mono_du += down - up

    monotonicity = max(mono_lr, mono_rl) + max(mono_ud, mono_du)

    corners = {
        "top_left": board[0][0],
        "top_right": board[0][-1],
        "bottom_left": board[-1][0],
        "bottom_right": board[-1][-1],
    }
    target_corner = max(corners.items(), key=lambda item: item[1])[0]
    matrix = SNAKE_WEIGHT_BY_CORNER[target_corner]

    snake_score = 0.0
    for r in range(SIZE):
        for c in range(SIZE):
            snake_score += log_values[r][c] * matrix[r][c]

    corner_bonus = -8.0
    if max_tile > 0:
        if max_tile in corners.values():
            corner_bonus = math.log2(max_tile) * 4.0

    max_tile_log = math.log2(max_tile) if max_tile else 0.0

    return (
        empty_cells * 360.0
        + merges * 140.0
        + smoothness * 14.0
        + monotonicity * 28.0
        + snake_score * 32.0
        + corner_bonus * 220.0
        + max_tile_log * 24.0
    )


def board_key(board: Board) -> Tuple[Tuple[int, ...], ...]:
    return tuple(tuple(row) for row in board)


def limited_empty_cells(board: Board, max_cells: int = MAX_CHANCE_BRANCHES) -> List[Tuple[int, int]]:
    cells = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
    if len(cells) <= max_cells:
        return cells

    # Prefer cells close to corners for stable board shaping.
    def corner_distance(cell: Tuple[int, int]) -> Tuple[int, int, int]:
        r, c = cell
        distance = min(
            r + c,
            r + (SIZE - 1 - c),
            (SIZE - 1 - r) + c,
            (SIZE - 1 - r) + (SIZE - 1 - c),
        )
        return (distance, r, c)

    cells.sort(key=corner_distance)
    return cells[:max_cells]


def expectimax(
    board: Board,
    depth: int,
    chance_turn: bool,
    cache: Dict[Tuple[Tuple[Tuple[int, ...], ...], int, bool], float],
    move_cache: Dict[Tuple[Tuple[int, ...], ...], List[Tuple[str, Board, int]]],
    eval_cache: Dict[Tuple[Tuple[int, ...], ...], float],
    deadline: float,
    strong_mode: bool,
) -> float:
    if time.monotonic() >= deadline:
        raise SearchTimeout

    key = (board_key(board), depth, chance_turn)
    cached = cache.get(key)
    if cached is not None:
        return cached

    board_state = key[0]

    if depth <= 0:
        value = eval_cache.get(board_state)
        if value is None:
            value = evaluate_board(board)
            eval_cache[board_state] = value
        cache[key] = value
        return value

    if chance_turn:
        if strong_mode:
            chance_branches = 4 if depth >= 4 else 6 if depth == 3 else MAX_CHANCE_BRANCHES
        else:
            chance_branches = 3 if depth >= 4 else 4 if depth == 3 else 6
        empties = limited_empty_cells(board, chance_branches)
        if not empties:
            value = expectimax(
                board,
                depth - 1,
                False,
                cache,
                move_cache,
                eval_cache,
                deadline,
                strong_mode,
            )
            cache[key] = value
            return value

        total = 0.0
        cell_weight = 1.0 / len(empties)

        # Deep layers ignore rare 4-spawns to keep turn time stable.
        spawn_options = ((2, 0.9), (4, 0.1)) if (strong_mode or depth <= 3) else ((2, 1.0),)
        for r, c in empties:
            if time.monotonic() >= deadline:
                raise SearchTimeout
            expected_for_cell = 0.0
            for spawned_value, prob in spawn_options:
                if time.monotonic() >= deadline:
                    raise SearchTimeout
                next_board = [row[:] for row in board]
                next_board[r][c] = spawned_value
                expected_for_cell += prob * expectimax(
                    next_board,
                    depth - 1,
                    False,
                    cache,
                    move_cache,
                    eval_cache,
                    deadline,
                    strong_mode,
                )
            total += cell_weight * expected_for_cell

        cache[key] = total
        return total

    moves = move_cache.get(board_state)
    if moves is None:
        computed_moves: List[Tuple[str, Board, int]] = []
        for direction in BOT_DIRECTIONS:
            moved_board, gain, moved = apply_move(board, direction)
            if moved:
                computed_moves.append((direction, moved_board, gain))
        moves = computed_moves
        move_cache[board_state] = moves

    if not moves:
        value = eval_cache.get(board_state)
        if value is None:
            value = evaluate_board(board)
            eval_cache[board_state] = value
        cache[key] = value
        return value

    best_value = -float("inf")
    for _, moved_board, _ in moves:
        if time.monotonic() >= deadline:
            raise SearchTimeout
        value = expectimax(
            moved_board,
            depth,
            True,
            cache,
            move_cache,
            eval_cache,
            deadline,
            strong_mode,
        )
        best_value = max(best_value, value)

    cache[key] = best_value
    return best_value


def choose_auto_move(
    board: Board,
    time_budget: float = AUTO_MOVE_TIME_BUDGET,
    strong_mode: bool = False,
) -> Optional[str]:
    empty_count = sum(1 for row in board for value in row if value == 0)
    if strong_mode:
        if empty_count >= 8:
            max_depth = 3
        elif empty_count >= 5:
            max_depth = 4
        else:
            max_depth = 5
    else:
        if empty_count >= 8:
            max_depth = 2
        elif empty_count >= 5:
            max_depth = 3
        else:
            max_depth = 4

    candidates: List[Tuple[str, Board, int]] = []
    for direction in BOT_DIRECTIONS:
        moved_board, gain, moved = apply_move(board, direction)
        if moved:
            candidates.append((direction, moved_board, gain))

    if not candidates:
        return None

    eval_cache: Dict[Tuple[Tuple[int, ...], ...], float] = {}
    move_cache: Dict[Tuple[Tuple[int, ...], ...], List[Tuple[str, Board, int]]] = {}

    def cached_eval(state: Board) -> float:
        key = board_key(state)
        value = eval_cache.get(key)
        if value is None:
            value = evaluate_board(state)
            eval_cache[key] = value
        return value

    move_cache[board_key(board)] = candidates[:]

    # Move ordering helps deeper iterations find good lines faster.
    candidates.sort(
        key=lambda item: (
            item[2],
            sum(1 for row in item[1] for value in row if value == 0),
            cached_eval(item[1]),
        ),
        reverse=True,
    )

    deadline = time.monotonic() + max(0.005, time_budget)
    best_move = candidates[0][0]
    best_value = -float("inf")

    for depth in range(1, max_depth + 1):
        cache: Dict[Tuple[Tuple[Tuple[int, ...], ...], int, bool], float] = {}
        depth_best_move = best_move
        depth_best_value = -float("inf")
        completed_depth = True

        for direction, moved_board, gain in candidates:
            if time.monotonic() >= deadline:
                completed_depth = False
                break
            try:
                value = expectimax(
                    moved_board,
                    depth,
                    True,
                    cache,
                    move_cache,
                    eval_cache,
                    deadline,
                    strong_mode,
                )
            except SearchTimeout:
                completed_depth = False
                break

            value += gain * 0.1
            if value > depth_best_value:
                depth_best_value = value
                depth_best_move = direction

        if completed_depth and depth_best_value > -float("inf"):
            best_move = depth_best_move
            best_value = depth_best_value
        else:
            break

        if time.monotonic() >= deadline:
            break

    # If timeout happened before depth 1 completed, use quick heuristic fallback.
    if best_value == -float("inf"):
        best_move = max(
            candidates,
            key=lambda item: (item[2], cached_eval(item[1])),
        )[0]

    return best_move


def choose_quick_move(board: Board) -> Optional[str]:
    candidates: List[Tuple[str, Board, int]] = []
    for direction in BOT_DIRECTIONS:
        moved_board, gain, moved = apply_move(board, direction)
        if moved:
            candidates.append((direction, moved_board, gain))

    if not candidates:
        return None

    return max(
        candidates,
        key=lambda item: (
            item[2],
            sum(1 for row in item[1] for value in row if value == 0),
            evaluate_board(item[1]),
        ),
    )[0]


def key_to_direction(key: int) -> Optional[str]:
    mapping = {
        curses.KEY_LEFT: "left",
        curses.KEY_RIGHT: "right",
        curses.KEY_UP: "up",
        curses.KEY_DOWN: "down",
        ord("a"): "left",
        ord("A"): "left",
        ord("d"): "right",
        ord("D"): "right",
        ord("w"): "up",
        ord("W"): "up",
        ord("s"): "down",
        ord("S"): "down",
        ord("h"): "left",
        ord("j"): "down",
        ord("k"): "up",
        ord("l"): "right",
    }
    return mapping.get(key)


def safe_addstr(stdscr: "curses._CursesWindow", y: int, x: int, text: str, attr: int = 0) -> None:
    height, width = stdscr.getmaxyx()
    if y < 0 or y >= height or x >= width:
        return
    if x < 0:
        text = text[-x:]
        x = 0
    if not text:
        return
    max_len = width - x
    if max_len <= 0:
        return
    try:
        stdscr.addstr(y, x, text[:max_len], attr)
    except curses.error:
        pass


def init_colors() -> Dict[int, int]:
    if not curses.has_colors():
        return {}

    try:
        curses.start_color()
        curses.use_default_colors()
    except curses.error:
        return {}

    value_levels = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    palette: Dict[int, Tuple[int, int]]
    if getattr(curses, "COLORS", 0) >= 256:
        # Yellow-only gradient: 2 is the lightest, then progressively deeper.
        yellow_bgs = [230, 229, 228, 227, 226, 220, 214, 208, 202, 172, 136]
        palette = {0: (236, 253)}
        for value, bg in zip(value_levels, yellow_bgs):
            if bg >= 220:
                fg = 94
            elif bg >= 202:
                fg = 230
            else:
                fg = 255
            palette[value] = (fg, bg)
    else:
        # Limited-color fallback keeps yellow family only.
        palette = {0: (curses.COLOR_BLACK, curses.COLOR_WHITE)}
        for idx, value in enumerate(value_levels):
            fg = curses.COLOR_BLACK if idx <= 5 else curses.COLOR_WHITE
            palette[value] = (fg, curses.COLOR_YELLOW)

    color_pairs: Dict[int, int] = {}
    pair_id = 1
    for value, (fg, bg) in palette.items():
        try:
            curses.init_pair(pair_id, fg, bg)
            color_pairs[value] = curses.color_pair(pair_id) | curses.A_BOLD
            pair_id += 1
        except curses.error:
            # Skip unsupported color combinations.
            continue
    return color_pairs


def tile_attr(value: int, color_pairs: Dict[int, int]) -> int:
    if not color_pairs:
        return curses.A_REVERSE if value else curses.A_DIM
    if value in color_pairs:
        return color_pairs[value]

    keys = sorted(k for k in color_pairs if k != 0)
    if not keys:
        return curses.A_NORMAL
    nearest = max((k for k in keys if k <= value), default=keys[-1])
    return color_pairs.get(nearest, curses.A_NORMAL)


def format_tile_lines(value: int, cell_w: int, cell_h: int) -> List[str]:
    if value <= 0:
        return []

    text = str(value)
    max_chars = max(1, cell_w - 2)
    if len(text) > max_chars:
        text = text[-max_chars:]
    return [text]


def draw(
    stdscr: "curses._CursesWindow",
    board: Board,
    score: int,
    best: int,
    status: str,
    color_pairs: Dict[int, int],
) -> None:
    stdscr.erase()
    height, width = stdscr.getmaxyx()

    cell_w = 15
    cell_h = 4
    gap_x = 1
    gap_y = 1
    board_w = SIZE * cell_w + (SIZE - 1) * gap_x
    board_h = SIZE * cell_h + (SIZE - 1) * gap_y
    top = 1
    left = max(0, (width - board_w) // 2)

    header = f"2048  Score:{score}  Best:{best}  Arrows/WASD move  R restart  Q quit"

    required_h = top + board_h + 2
    required_w = max(board_w + 2, len(header) + 2)

    if height < required_h or width < required_w:
        msg = f"Resize terminal to at least {required_w}x{required_h}. Current: {width}x{height}"
        safe_addstr(stdscr, 0, 0, msg, curses.A_BOLD)
        safe_addstr(stdscr, 2, 0, "Press Q to quit.", curses.A_DIM)
        stdscr.refresh()
        return

    safe_addstr(stdscr, 0, (width - len(header)) // 2, header, curses.A_BOLD)

    for r in range(SIZE):
        for c in range(SIZE):
            value = board[r][c]
            attr = tile_attr(value, color_pairs)
            x = left + c * (cell_w + gap_x)
            y = top + r * (cell_h + gap_y)
            for dy in range(cell_h):
                safe_addstr(stdscr, y + dy, x, " " * cell_w, attr)

            lines = format_tile_lines(value, cell_w, cell_h)
            if lines:
                text_top = y + (cell_h - len(lines)) // 2
                for i, line in enumerate(lines):
                    text_x = x + (cell_w - len(line)) // 2
                    safe_addstr(stdscr, text_top + i, text_x, line, attr | curses.A_BOLD)

    safe_addstr(stdscr, top + board_h + 1, (width - len(status)) // 2, status, curses.A_BOLD)
    stdscr.refresh()


def run_game(stdscr: "curses._CursesWindow") -> None:
    try:
        curses.curs_set(0)
    except curses.error:
        pass
    stdscr.keypad(True)

    color_pairs = init_colors()

    board = new_board()
    score = 0
    best = 0
    won = False
    game_over = False
    status = "Join tiles and reach 2048."

    while True:
        draw(stdscr, board, score, best, status, color_pairs)
        key = stdscr.getch()

        if key in (ord("q"), ord("Q")):
            return

        if key in (ord("r"), ord("R"), ord("n"), ord("N")):
            board = new_board()
            score = 0
            won = False
            game_over = False
            status = "New game started."
            continue

        direction = key_to_direction(key)
        if direction is None:
            status = "Use arrows or WASD. Press R to restart, Q to quit."
            continue

        if game_over:
            status = "Game over. Press R to restart or Q to quit."
            continue

        new_board_state, gain, moved = apply_move(board, direction)
        if not moved:
            status = "That move does nothing."
            continue

        board = new_board_state
        score += gain
        best = max(best, score)
        add_random_tile(board)

        if not won and reached_target(board):
            won = True
            status = "You made 2048! Keep playing, or press R to restart."
        elif not can_move(board):
            game_over = True
            status = "Game over! Press R to restart or Q to quit."
        else:
            status = f"Moved {direction}."


def run_auto_game(stdscr: "curses._CursesWindow", speed: float, strong_mode: bool, engine: str) -> None:
    try:
        curses.curs_set(0)
    except curses.error:
        pass
    stdscr.keypad(True)
    stdscr.nodelay(True)

    speed = max(0.1, speed)
    step_delay = 1.0 / speed
    nneonneo_timeout = AUTO_MOVE_MAX_THINK_TIME
    base_budget = AUTO_MOVE_TIME_BUDGET * (1.6 if strong_mode else 1.0)
    search_budget = min(base_budget, max(0.05, step_delay * (0.9 if strong_mode else 0.75)))

    active_engine = "local"
    nneonneo_engine: Optional[TimedNneonneoEngine] = None
    engine_notice = ""
    if engine in ("auto", "nneonneo"):
        nneonneo_engine, err = load_nneonneo_engine(move_timeout=nneonneo_timeout)
        if nneonneo_engine is not None:
            active_engine = "nneonneo"
        else:
            active_engine = "local"
            if engine == "nneonneo":
                engine_notice = f"nneonneo unavailable ({err}); using local bot."
            else:
                engine_notice = f"auto engine fell back to local ({err})."

    color_pairs = init_colors()

    board = new_board()
    score = 0
    best = 0
    won = False
    game_over = False
    mode_label = f"{active_engine}{'+strong' if strong_mode and active_engine == 'local' else ''}"
    status = (
        f"{engine_notice} " if engine_notice else ""
    ) + f"Auto mode [{mode_label}] ({speed:.1f} moves/sec). Q quit, R restart."
    next_move_time = time.monotonic()
    try:
        while True:
            draw(stdscr, board, score, best, status, color_pairs)

            key = stdscr.getch()
            if key in (ord("q"), ord("Q")):
                return

            if key in (ord("r"), ord("R"), ord("n"), ord("N")):
                board = new_board()
                score = 0
                won = False
                game_over = False
                status = f"Auto mode [{mode_label}] ({speed:.1f} moves/sec). Restarted."
                next_move_time = time.monotonic()
                continue

            if game_over:
                time.sleep(0.05)
                continue

            now = time.monotonic()
            if now < next_move_time:
                time.sleep(min(0.05, next_move_time - now))
                continue

            move_scheduled_at = next_move_time
            think_started_at = time.monotonic()
            fallback_reason = ""
            fallback_used = False

            if active_engine == "nneonneo" and nneonneo_engine is not None:
                direction = nneonneo_engine.choose_move(board, timeout=nneonneo_timeout)
                if direction is None:
                    fallback_used = True
                    fallback_reason = nneonneo_engine.last_error or "no move"
                    elapsed = time.monotonic() - think_started_at
                    remaining_budget = max(0.02, nneonneo_timeout - elapsed)
                    local_budget = min(search_budget, remaining_budget)
                    if local_budget <= 0.08:
                        direction = choose_quick_move(board)
                    else:
                        direction = choose_auto_move(
                            board,
                            time_budget=local_budget,
                            strong_mode=True,
                        )
            else:
                direction = choose_auto_move(board, search_budget, strong_mode=strong_mode)

            think_ms = int((time.monotonic() - think_started_at) * 1000)

            if direction is None:
                game_over = True
                status = "Auto-play stuck. Press R to restart or Q to quit."
                continue

            new_board_state, gain, moved = apply_move(board, direction)
            if not moved:
                next_move_time = move_scheduled_at + step_delay
                if next_move_time < time.monotonic():
                    next_move_time = time.monotonic()
                status = "Auto-play skipped an invalid move."
                continue

            board = new_board_state
            score += gain
            best = max(best, score)
            add_random_tile(board)

            if not won and reached_target(board):
                won = True
                status = f"Auto reached 2048 in {think_ms}ms. Continuing..."
            elif not can_move(board):
                game_over = True
                status = "Auto-play finished (game over). Press R or Q."
            elif fallback_used:
                status = f"Auto moved {direction} ({think_ms}ms, local fallback: {fallback_reason})."
            else:
                status = f"Auto moved {direction} ({think_ms}ms)."

            next_move_time = move_scheduled_at + step_delay
            if next_move_time < time.monotonic():
                next_move_time = time.monotonic()
    finally:
        if nneonneo_engine is not None:
            nneonneo_engine.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Play 2048 in the terminal.")
    parser.add_argument("--auto", action="store_true", help="Run autoplay bot.")
    parser.add_argument("--strong", action="store_true", help="Use stronger but heavier auto-search.")
    parser.add_argument(
        "--engine",
        choices=("local", "nneonneo", "auto"),
        default="local",
        help="Autoplay engine. 'nneonneo' uses /usr/local/etc/2048-ai/bin/2048.so.",
    )
    parser.add_argument(
        "--speed",
        type=float,
        default=AUTO_DEFAULT_SPEED,
        help="Auto mode moves per second (default: 2).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    auto_mode = args.auto or args.engine != "local" or "--engine" in sys.argv
    if auto_mode:
        curses.wrapper(run_auto_game, args.speed, args.strong, args.engine)
    else:
        curses.wrapper(run_game)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
