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

def display_leds(direction, steps, on):
    clear_leds()  # LED 상태를 변경하기 전에 모든 LED를 초기화
    brightness = 50 if on else 0
    if direction == "left" or direction == "both":
        for i in range(42):
            pixels[i] = (brightness, 0, 0) if on else (0, 0, 0)
    if direction == "right" or direction == "both":
        for i in range(42, 84):
            pixels[i] = (0, 0, brightness) if on else (0, 0, 0)
    pixels.write()

def control_leds():
    flash_interval = 500  # LED 깜빡임 간격을 500ms로 설정
    last_flash_time = time.ticks_ms()
    active_tilt = None
    led_on = False
    low_speed_threshold = 10  # 임계 각속도 값 설정 (예: 저속)
    high_threshold = 30  # 높은 임계값
    low_threshold = 20  # 낮은 임계값, hysteresis 적용

    while True:
        acc_x, acc_y, acc_z = mpu.accel.x, mpu.accel.y, mpu.accel.z
        gyro_y = mpu.gyro.y
        _, angle_y = calculate_angle(acc_x, acc_y, acc_z)

        print("Current tilt angle Y-axis:", angle_y, "Gyro Y-axis speed:", gyro_y)

        if angle_y > high_threshold:
            direction = "right"
        elif angle_y < -high_threshold:
            direction = "left"
        elif abs(gyro_y) < low_speed_threshold:
            direction = "both"  # 저속일 때 양쪽 LED 깜빡임
        else:
            direction = None

        if direction:
            if active_tilt != direction:
                active_tilt = direction
                led_on = True
                last_flash_time = time.ticks_ms()  # LED 켜기 시작 시간 리셋
                display_leds(direction, 1, led_on)
            elif time.ticks_diff(time.ticks_ms(), last_flash_time) > flash_interval:
                last_flash_time = time.ticks_ms()
                led_on = not led_on
                display_leds(direction, 1, led_on)
        else:
            if active_tilt:
                clear_leds()
                active_tilt = None
                led_on = False

        time.sleep(0.05)

# 메인 함수 호출
control_leds()



