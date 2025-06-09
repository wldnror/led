#!/usr/bin/env python3
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time

options = RGBMatrixOptions()
options.rows = 32
options.cols = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'

# ↓ 권한 드롭 방지
options.drop_privileges = False

# ↓ 만약 라이브러리에서 지원한다면 이 옵션으로 대체
# options.disable_hardware_pulse = True

matrix = RGBMatrix(options=options)

try:
    colors = [(255,0,0),(0,255,0),(0,0,255)]
    while True:
        for c in colors:
            matrix.Fill(*c)
            time.sleep(1)
finally:
    matrix.Clear()
