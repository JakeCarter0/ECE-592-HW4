import RPi.GPIO as gpio
import time
import threading
import logging

gpio.setmode(gpio.BOARD)

logging.basicConfig(level=logging.DEBUG,
                    format='%(thread)d (%(threadName)-12s) %(message)s',
                    )
LEDs = [8, 10]
SWs = [12, 16]
gpio.setup(LEDs, gpio.OUT, initial = gpio.LOW)
gpio.setup(SWs, gpio.IN, pull_up_down = gpio.PUD_UP)

#gpio.setup(LED2, gpio.OUT, initial = gpio.LOW)

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

def setLED(led, t, sw):
    logging.debug("Starting")
    while(True):
        gpio.output(led, True)
        time.sleep(t)
        gpio.output(led, False)
        time.sleep(t)
        input_state = gpio.input(sw)
        if (input_state == False):
            break
    logging.debug("Exiting")
        
t1 = threading.Thread(name = "led1", target=setLED, args=(LEDs[0], 1, SWs[0]))
t1.setDaemon(True)
t2 = threading.Thread(name = "led2", target=setLED, args=(LEDs[1], 2, SWs[1]))
t1.start()
t2.start()
