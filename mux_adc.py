# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import spidev
import json
from http_test import *


class Vol:
    def __init__(self):
        self.result = 0

    def ReadVol(self, vol):
        adc = spi.xfer2([1, (8 + vol) << 4, 0])
        self.result = ((adc[1] & 3) << 8) + adc[2]
        return self.result

##spi설정
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

##핀설정
s0 = 11
s1 = 12
s2 = 13
s3 = 16
mcp3008 = 0

##GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(s0, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(s1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(s2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(s3, GPIO.OUT, initial=GPIO.LOW)

if __name__ == '__main__':
    my_vol = Vol()
    my_tran = Http()
    try:
        while True:
            GPIO.output(s0, GPIO.HIGH)
            GPIO.output(s1, GPIO.LOW)

            a_1 = my_vol.ReadVol(mcp3008)
            print('readvol_1 : ', a_1, 'Voltage:', 3.3 * a_1 / 1024)
            my_tran.response(a_1)

            GPIO.output(s0, GPIO.LOW)
            GPIO.output(s1, GPIO.HIGH)
            time.sleep(2)

            a_2 = my_vol.ReadVol(mcp3008)
            print('readvol_2 : ', a_2, 'Voltage:', 3.3 * a_2 / 1024)

            GPIO.output(s0, GPIO.HIGH)
            time.sleep(2)

            a_3 = my_vol.ReadVol(mcp3008)
            print('readvol_3 : ', a_3, 'Voltage:', 3.3 * a_3 / 1024)

            time.sleep(2)

    except KeyboardInterrupt:
        pass
    GPIO.cleanup()



