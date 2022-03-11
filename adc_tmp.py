# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import spidev
import json
from http_test import *


class Tmp:
    def __init__(self):
        self.result = 0

    def ReadTmp(self, tmp):
        adc = spi.xfer2([1, (8 + tmp) << 4, 0])
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
tmp36=0

##GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(s0, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(s1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(s2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(s3, GPIO.OUT, initial=GPIO.LOW)

if __name__ == '__main__':
    my_tmp = Tmp()
    try:
        while True:
            GPIO.output(s0, GPIO.HIGH)
            GPIO.output(s1, GPIO.LOW)

            t_1 = my_tmp.ReadTmp(tmp36)
            print('volts_1 : ', (t_1 * 3.3)/float(1023), 'temp_1:', ((t_1 * 330)/float(1023))-50)

            GPIO.output(s0, GPIO.LOW)
            GPIO.output(s1, GPIO.HIGH)
            time.sleep(2)

            t_2 = my_tmp.ReadTmp(tmp36)
            print('volts_2 : ', (t_2 * 3.3) / float(1023), 'temp_2:', ((t_2 * 330) / float(1023)) - 50)

            GPIO.output(s0, GPIO.HIGH)
            time.sleep(2)

            t_3 = my_tmp.ReadTmp(tmp36)
            print('volts_3 : ', (t_3 * 3.3) / float(1023), 'temp_3:', ((t_3 * 330) / float(1023)) - 50)

            time.sleep(2)

    except KeyboardInterrupt:
        pass
    GPIO.cleanup()
