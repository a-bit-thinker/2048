#!/usr/bin/env python3
"""Clone and build nneonneo/2048-ai into /usr/local/etc/2048-ai."""

import os
import subprocess
import sys


REPO_URL = "https://github.com/nneonneo/2048-ai.git"


def run(cmd: list[str], cwd: str | None = None) -> int:
    print("+", " ".join(cmd))
    return subprocess.call(cmd, cwd=cwd)


def main() -> int:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.join(base_dir, "2048-ai")

    if not os.path.isdir(repo_dir):
        if run(["git", "clone", REPO_URL, repo_dir]) != 0:
            print("Clone failed. Check network/DNS and try again.", file=sys.stderr)
            return 1
    else:
        print(f"Repo already exists: {repo_dir}")

    configure = os.path.join(repo_dir, "configure")
    if os.path.isfile(configure):
        if run(["sh", "./configure"], cwd=repo_dir) != 0:
            print("configure failed.", file=sys.stderr)
            return 1

    if run(["make", "-j"], cwd=repo_dir) != 0:
        print("build failed.", file=sys.stderr)
        return 1

    bin_path = os.path.join(repo_dir, "bin", "2048")
    if not os.path.isfile(bin_path):
        print(f"Build finished but missing binary: {bin_path}", file=sys.stderr)
        return 1

    print(f"Installed successfully: {bin_path}")
    print("Run autoplay with: python3 auto_play_2048.py --engine nneonneo")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
