import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
LED = 8
LED2 = 18
SW1 = 10
SW2 = 16
gpio.setup(LED, gpio.OUT)
gpio.setup(LED2, gpio.OUT)


def waitforbutton(t):
    gpio.setup(SW1, gpio.IN, pull_up_down = gpio.PUD_UP) 
    channel = gpio.wait_for_edge(SW1, gpio.RISING, timeout=t*1000)
    if channel is None:
        print('timeout')
    else:
        print('button pressed')

def eventdetect():
    gpio.setup(SW2, gpio.IN, pull_up_down = gpio.PUD_UP)
    gpio.add_event_detect(SW2, gpio.BOTH, callback=my_callback_one, bouncetime=100)
    while(True):
        time.sleep(0.2)

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

def buttonpress():
        gpio.setup(SW2, gpio.IN, pull_up_down = gpio.PUD_UP)
        gpio.add_event_detect(SW2, gpio.FALLING, callback=isitpressed, bouncetime=100)
        while(True):
                time.sleep(0.5)
                gpio.output(LED2, True)
                time.sleep(0.5)
                gpio.output(LED2, False)

def isitpressed(channel):
    i = 0
    while(gpio.input(SW2) == gpio.LOW):
        #time.sleep(0.2)
        time.sleep(0.2)
        gpio.output(LED, True)
        time.sleep(0.2)
        gpio.output(LED, False)
        i = i + 0.4
        if i>3:
            print("button pressed for 3 seconds")


def main():
    import sys
    if sys.argv[1:]:
        t = int(sys.argv[1])
        waitforbutton(t)
    else:
        buttonpress()

if __name__ == "__main__":
    main()
