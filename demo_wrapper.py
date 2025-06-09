#!/usr/bin/env python3
import subprocess
import sys

def main():
    cmd = [
        "sudo", "/home/user/rpi-rgb-led-matrix/examples-api-use/demo",
        "-D", "0",
        "--led-no-hardware-pulse",
        "--led-rows=32",
        "--led-cols=64",
        "--led-chain=2",
        "--led-parallel=1"
    ]
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        # Ctrl-C 로 종료 시 LED 리셋
        pass

if __name__ == "__main__":
    main()
