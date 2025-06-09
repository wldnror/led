from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time

# 설정 옵션
options = RGBMatrixOptions()
options.rows = 32           # 디스플레이 행 수 (32로 설정)
options.cols = 32           # 디스플레이 열 수 (32로 설정)
options.chain_length = 1    # 연결된 패널의 개수
options.parallel = 1        # 병렬 연결 개수 (기본 1)
options.hardware_mapping = 'adafruit-hat-pwm'  # 라즈베리파이 4, 5는 일반적으로 이 옵션 필요
options.gpio_slowdown = 4  # 라즈베리파이 4,5에 종종 필요한 설정

# RGBMatrix 인스턴스 생성
matrix = RGBMatrix(options=options)
canvas = matrix.CreateFrameCanvas()

# 텍스트 및 색상 설정
font = graphics.Font()
font.LoadFont("../rpi-rgb-led-matrix/fonts/7x13.bdf")
textColor = graphics.Color(255, 0, 0)

pos = canvas.width
text = "Hello HUB75!"

try:
    while True:
        canvas.Clear()
        len = graphics.DrawText(canvas, font, pos, 20, textColor, text)
        pos -= 1
        if (pos + len < 0):
            pos = canvas.width

        time.sleep(0.05)
        canvas = matrix.SwapOnVSync(canvas)

except KeyboardInterrupt:
    matrix.Clear()
