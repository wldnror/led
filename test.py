#!/usr/bin/env python3
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time

options = RGBMatrixOptions()
options.rows = 32
options.cols = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'

# ↓ 아래 두 줄 추가
options.led_no_hardware_pulse = True
options.drop_privileges    = False

matrix = RGBMatrix(options=options)

try:
    colors = [(255,0,0),(0,255,0),(0,0,255)]
    while True:
        for c in colors:
            matrix.Fill(*c)
            time.sleep(1)
finally:
    matrix.Clear()
