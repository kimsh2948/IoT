import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


try:
    while 1:
        GPIO.output(23, False)
        GPIO.output(24, False)
        time.sleep(1)
        GPIO.output(23, False)
        GPIO.output(24, False)
        time.sleep(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()