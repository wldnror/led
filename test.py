#!/usr/bin/env python3
import argparse
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions

def parse_args():
    parser = argparse.ArgumentParser(
        description="Test an RGB LED matrix on Raspberry Pi 5 with custom options"
    )
    parser.add_argument("--led-rows", type=int, default=32, help="Rows")
    parser.add_argument("--led-cols", type=int, default=32, help="Cols")
    parser.add_argument("--led-chain", type=int, default=1, help="Chains")
    parser.add_argument("--led-parallel", type=int, default=1, help="Parallels")
    parser.add_argument(
        "--led-no-hardware-pulse", action="store_true",
        help="Disable hardware pulse generator (use software timing)"
    )
    return parser.parse_args()

def main():
    args = parse_args()

    options = RGBMatrixOptions()
    options.rows            = args.led_rows
    options.cols            = args.led_cols
    options.chain_length    = args.led_chain
    options.parallel        = args.led_parallel
    options.drop_privileges = False

    # 하드웨어 펄스 비활성화
    if args.led_no_hardware_pulse:
        options.hardware_mapping = "regular"
        # 가능한 속성들 모두 시도
        if hasattr(options, 'disable_hardware_pulse'):
            options.disable_hardware_pulse = True
        if hasattr(options, 'hardware_pulse'):
            options.hardware_pulse = False
        if hasattr(options, 'disable_hw_pulse'):
            options.disable_hw_pulse = True

    matrix = RGBMatrix(options=options)

    try:
        for color in [(255,0,0),(0,255,0),(0,0,255)]:
            matrix.Fill(*color)
            time.sleep(1)
    finally:
        matrix.Clear()

if __name__ == "__main__":
    main()
