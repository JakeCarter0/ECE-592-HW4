import RPi.GPIO as gpio
import time

LED = 8
SW = 16

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(SW, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(LED, gpio.OUT)
count = 0
while True:
    c = gpio.wait_for_edge(SW, gpio.BOTH)
    if c is None:
        print("timeout occured")
    else:
        count = count + 1
        print('Edge detected on the button', count)
            
    
