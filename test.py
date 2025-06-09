#!/usr/bin/env python3
import argparse
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time

# 1) argparse 로 플래그 정의
parser = argparse.ArgumentParser()
parser.add_argument("--led-rows",    type=int,   default=32)
parser.add_argument("--led-cols",    type=int,   default=32)
parser.add_argument("--led-chain",   type=int,   default=1)
parser.add_argument("--led-parallel",type=int,   default=1)
parser.add_argument("--led-no-hardware-pulse", action="store_true")
args = parser.parse_args()

# 2) 옵션에 반영
options = RGBMatrixOptions()
options.rows            = args.led_rows
options.cols            = args.led_cols
options.chain_length    = args.led_chain
options.parallel        = args.led_parallel
options.drop_privileges = False
if args.led_no_hardware_pulse:
    options.hardware_mapping = 'regular'  # hardware pulse 대신 소프트웨어로
    options.pwm_lsb_nanoseconds = 0       # 예시로 세팅

matrix = RGBMatrix(options=options)

# 이하 동일…
