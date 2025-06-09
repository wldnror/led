#!/usr/bin/env python3
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time

options = RGBMatrixOptions()
options.rows            = 32            # 매트릭스 행 수
options.cols            = 32            # 매트릭스 열 수
options.chain_length    = 1             # 체인된 패널 수
options.parallel        = 1             # 병렬 연결 수
options.hardware_mapping = 'regular'    # 단순 변환 보드일 땐 'regular'
options.drop_privileges = False         # 권한 드롭 방지

matrix = RGBMatrix(options=options)

try:
    # 빨강 → 초록 → 파랑 순으로 깜빡이기
    for color in [(255,0,0),(0,255,0),(0,0,255)]:
        matrix.Fill(*color)
        time.sleep(1)
finally:
    matrix.Clear()
