import RPi.GPIO as gpio
import time
import sys

gpio.setmode(gpio.BOARD)

print(gpio.getmode())

gpio.setwarnings(False)

LED = 12
LED2 = 32
gpio.setup(LED, gpio.OUT, initial=gpio.LOW)
gpio.setup(LED2, gpio.OUT, initial=gpio.LOW)

p = gpio.PWM(LED, 100)
p.start(90)
input('Press return to stop:')   # use raw_input for Python 2
p.stop()
gpio.cleanup()