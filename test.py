#!/usr/bin/env python3
import argparse
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions

def parse_args():
    parser = argparse.ArgumentParser(
        description="Test an RGB LED matrix on Raspberry Pi 5 with custom options"
    )
    parser.add_argument(
        "--led-rows", type=int, default=32,
        help="Number of rows of the matrix (default: 32)"
    )
    parser.add_argument(
        "--led-cols", type=int, default=32,
        help="Number of columns of the matrix (default: 32)"
    )
    parser.add_argument(
        "--led-chain", type=int, default=1,
        help="Number of daisy-chained panels (default: 1)"
    )
    parser.add_argument(
        "--led-parallel", type=int, default=1,
        help="Number of parallel chains (default: 1)"
    )
    parser.add_argument(
        "--led-no-hardware-pulse", action="store_true",
        help="Disable hardware pulse generator (use software timing)"
    )
    return parser.parse_args()

def main():
    args = parse_args()

    # Configure RGBMatrix options
    options = RGBMatrixOptions()
    options.rows            = args.led_rows
    options.cols            = args.led_cols
    options.chain_length    = args.led_chain
    options.parallel        = args.led_parallel
    options.drop_privileges = False

    if args.led_no_hardware_pulse:
        # Force software PWM/timing
        options.hardware_mapping    = "regular"
        options.pwm_lsb_nanoseconds = 0

    matrix = RGBMatrix(options=options)

    try:
        # Cycle through red → green → blue
        for color in [(255, 0, 0), (0, 255, 0), (0, 0, 255)]:
            matrix.Fill(*color)
            time.sleep(1)
    finally:
        # Clear display on exit
        matrix.Clear()

if __name__ == "__main__":
    main()
