#!/usr/bin/env python3
import subprocess

def main():
    demo_bin = "/home/user/rpi-rgb-led-matrix/examples-api-use/demo"

    cmd = [
        "sudo",                # 여기서 sudo로 권한 확보
        demo_bin,
        "-D", "0",                     # 회전 사각형 데모
        "--led-no-hardware-pulse",     # 하드웨어 펄스 비활성화
        "--led-no-drop-privs",         # 권한 드롭 방지
        "--led-rows", "32",
        "--led-cols", "64",
        "--led-chain", "2",
        "--led-parallel", "1"
    ]

    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
