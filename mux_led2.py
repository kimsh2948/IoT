import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)

try:
    while 1:
        GPIO.output(23, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(23, GPIO.LOW)

        time.sleep(0.5)

        GPIO.output(24, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(24, GPIO.LOW)
except KeyboardInterrupt:
    pass

GPIO.cleanup()


