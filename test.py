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

    # Initialize matrix (hardware pulse used by default)
    matrix = RGBMatrix(options=options)

    try:
        # Cycle through red → green → blue
        for color in [(255, 0, 0), (0, 255, 0), (0, 0, 255)]:
            matrix.Fill(*color)
            time.sleep(1)
    finally:
        matrix.Clear()

if __name__ == "__main__":
    main()
