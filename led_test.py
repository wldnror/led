from imu import MPU6050
import time
from machine import Pin, I2C
import neopixel
import math

# I2C 설정
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
mpu = MPU6050(i2c)

# NeoPixel LED 설정
pixel_pin = Pin(22)
num_pixels = 84
pixels = neopixel.NeoPixel(pixel_pin, num_pixels)

def calculate_angle(acc_x, acc_y, acc_z):
    angle_x = math.atan2(acc_x, math.sqrt(acc_y**2 + acc_z**2)) * 180 / math.pi
    angle_y = math.atan2(acc_y, math.sqrt(acc_x**2 + acc_z**2)) * 180 / math.pi
    return angle_x, angle_y

def clear_leds():
    for i in range(num_pixels):
        pixels[i] = (0, 0, 0)
    pixels.write()

def display_leds(group, on):
    clear_leds()  # 모든 LED를 초기화
    brightness = 50 if on else 0

    # 그룹 번호에 따라 LED 점등 범위 설정
    if group == 1:
        start, end = 0, 21
    elif group == 2:
        start, end = 21, 42
    elif group == 3:
        start, end = 42, 63
    elif group == 4:
        start, end = 63, 84

    for i in range(start, end):
        pixels[i] = (brightness, brightness // 3, 0) if on else (0, 0, 0)

    pixels.write()  # 변경된 LED 상태를 쓰기

def main():
    while True:
        try:
            group = int(input("1 ~ 4 사이의 숫자를 입력하세요 (LED 그룹 선택): "))
            if group not in [1, 2, 3, 4]:
                print("1 ~ 4 사이의 숫자만 입력 가능합니다.")
                continue
        except ValueError:
            print("유효하지 않은 입력입니다. 숫자를 입력해주세요.")
            continue

        # 선택된 그룹의 LED 켜기
        display_leds(group, True)
        time.sleep(3)  # 3초 동안 켜짐 유지

        # 선택된 그룹의 LED 끄기
        display_leds(group, False)

if __name__ == "__main__":
    main()
