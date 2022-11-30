import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
LED = 8
SW1 = 10
SW2 = 16
gpio.setup(SW2, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(LED, gpio.OUT)

def my_callback_one(channel):
    i = 0
    while(gpio.input(SW2) == gpio.LOW):
        gpio.output(LED, True)
        time.sleep(0.5)
        i = i+0.5
        gpio.output(LED, False)
        time.sleep(0.5)
        i = i+0.5
        if i >= 3 and i < 3.5:
            print("more than 3 seconds")
    if gpio.input(SW2) == gpio.HIGH:
        print('released')
        gpio.output(LED, False)

gpio.add_event_detect(SW2, gpio.BOTH, callback=my_callback_one, bouncetime=100)
while(True):
    time.sleep(0.2)