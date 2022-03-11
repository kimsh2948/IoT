# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
#BCM 번호 체계를 사용
GPIO.setmode(GPIO.BCM)
sensor = 23

GPIO.setup(sensor, GPIO.IN)
print("Waitig for sensor to settle")
time.sleep(2)
print("Detecting motion")

while True:
    if GPIO.input(sensor):
        print("Motion detected")
        time.sleep(1)
    else:
        print("No motion")
	time.sleep(1)
