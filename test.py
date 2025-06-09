#!/usr/bin/env python3
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time

# 매트릭스 옵션 설정
options = RGBMatrixOptions()
options.rows = 32       # 매트릭스 행 수
options.cols = 32       # 매트릭스 열 수
options.chain_length = 1  # 체인 연결된 패널 수
options.parallel = 1      # 병렬 연결 수
options.hardware_mapping = 'adafruit-hat'  # 변환 보드 모델에 맞춰 변경

matrix = RGBMatrix(options=options)

try:
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # R, G, B
    while True:
        for color in colors:
            matrix.Fill(*color)  # 화면 전체를 해당 색으로 채움
            time.sleep(1)
finally:
    matrix.Clear()
