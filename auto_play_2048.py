#!/usr/bin/env python3
"""Autoplay launcher with optional nneonneo/2048-ai engine."""

import argparse
import os
import subprocess
import sys
from typing import Optional


def run_cmd(cmd: list[str], cwd: Optional[str] = None) -> int:
    return subprocess.call(cmd, cwd=cwd)


def nneonneo_repo_dir(base_dir: str) -> str:
    return os.path.join(base_dir, "2048-ai")


def nneonneo_bin_path(base_dir: str) -> str:
    return os.path.join(nneonneo_repo_dir(base_dir), "bin", "2048")


def try_build_nneonneo(base_dir: str) -> bool:
    repo_dir = nneonneo_repo_dir(base_dir)
    if not os.path.isdir(repo_dir):
        return False

    configure = os.path.join(repo_dir, "configure")
    if os.path.isfile(configure):
        if run_cmd(["sh", "./configure"], cwd=repo_dir) != 0:
            return False

    if run_cmd(["make", "-j"], cwd=repo_dir) != 0:
        return False

    return os.path.isfile(nneonneo_bin_path(base_dir))


def run_nneonneo(base_dir: str) -> int:
    bin_path = nneonneo_bin_path(base_dir)
    if not os.path.isfile(bin_path):
        if not try_build_nneonneo(base_dir):
            return 127
    return run_cmd([bin_path], cwd=nneonneo_repo_dir(base_dir))


def run_local(base_dir: str, speed: float, strong: bool) -> int:
    game_path = os.path.join(base_dir, "terminal_2048.py")
    cmd = [sys.executable, game_path, "--auto", "--engine", "local", "--speed", str(speed)]
    if strong:
        cmd.append("--strong")
    return run_cmd(cmd, cwd=base_dir)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Launch 2048 autoplay.")
    parser.add_argument(
        "--engine",
        choices=("auto", "nneonneo", "local"),
        default="auto",
        help="autoplay engine: auto tries nneonneo first, then local fallback.",
    )
    parser.add_argument("--speed", type=float, default=2.0, help="local engine moves/sec (default: 2).")
    parser.add_argument("--strong", action="store_true", help="use stronger local search mode.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    base_dir = os.path.dirname(os.path.abspath(__file__))

    if args.engine in ("auto", "nneonneo"):
        code = run_nneonneo(base_dir)
        if code == 0:
            return 0
        if args.engine == "nneonneo":
            print(
                "nneonneo engine not available. Put repo at /usr/local/etc/2048-ai "
                "and build it (run install_nneonneo_2048_ai.py).",
                file=sys.stderr,
            )
            return 1
        print("nneonneo engine unavailable, falling back to local bot.", file=sys.stderr)

    return run_local(base_dir, speed=args.speed, strong=args.strong or args.engine == "auto")


if __name__ == "__main__":
    raise SystemExit(main())
