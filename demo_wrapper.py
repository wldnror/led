#!/usr/bin/env python3
import subprocess

def main():
    # demo 바이너리 경로는 실제 위치에 맞게 수정하세요
    demo_bin = "/home/user/rpi-rgb-led-matrix/examples-api-use/demo"

    cmd = [
        "sudo", demo_bin,
        "-D", "0",                     # 회전 사각형 데모
        "--led-no-hardware-pulse", "1",
        "--led-no-drop-privs", "1",    # 권한 드롭 방지
        "--led-rows", "32",
        "--led-cols", "64",
        "--led-chain", "2",
        "--led-parallel", "1"
    ]

    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        # Ctrl-C 시 LED 초기화 후 종료
        pass

if __name__ == "__main__":
    main()
