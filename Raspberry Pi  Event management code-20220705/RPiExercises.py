import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(10, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(8, gpio.OUT)


while True:
    input_state = gpio.input(10)
    if input_state == False:
        print('Button Pressed')
        gpio.output(8, True)
        time.sleep(1)
        gpio.output(8, False)
        time.sleep(1)
    else:
        print("Button not pressed")        
        