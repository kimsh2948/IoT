import _wingpio as gpio
import time
import itertools

pins = (23, 24)
pinValue = gpio.HIGH

for pin in pins:
    gpio.setup(pin, gpio.OUT, gpio.PUD_OFF, gpio.HIGH)

lst = list(itertools.product([0, 1], repeat=len(pins)))

while True:
    for setup in lst:
        for i, pin in enumerate(pins):
            gpio.output(pin, setup[i])
        time.sleep(1)
    time.sleep(5)

gpio.cleanup()