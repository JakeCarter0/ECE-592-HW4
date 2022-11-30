"""
Created on July 10 2022

@author:
PiE Homework 4
Server to run on Raspberry Pi that detects switch inputs and outputs signals on connected LEDs
This code is designed to send updates to Client.py with swithc states every second
"""


import RPi.GPIO as gpio
import time
import threading
import socket
import subprocess
import os

HOST = subprocess.check_output(["hostname", "-I"]).decode()[0:-2]

PORT = 3454

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
rLED = 16
gLED = 18
SW1 = 8
SW2 = 10
SW3 = 12
gpio.setup(SW1, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(SW2, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(SW3, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(rLED, gpio.OUT)
gpio.setup(gLED, gpio.OUT)

global sw1Status
global sw2Status
global gLEDTmr
global rLEDTmr

sw1Status = "Released"
sw2Status = "Released"
gLEDTmr = 0
rLEDTmr = 0

def SW1_callback(channel):
    global sw1Status
    global rLEDTmr
    time.sleep(.05)
    if gpio.input(SW1) == gpio.LOW:
        rLEDTmr = 200
        sw1Status = "Pressed"
    elif gpio.input(SW1) == gpio.HIGH:
        rLEDTmr = 0
        gpio.output(rLED, False)
        sw1Status = "Released"

def SW2_callback(channel):
    global sw2Status
    global gLEDTmr
    time.sleep(.05)
    if gpio.input(SW2) == gpio.LOW:
        gLEDTmr = 100
        sw2Status = "Pressed"
    if gpio.input(SW2) == gpio.HIGH:
        gLEDTmr = 0
        gpio.output(gLED, False)
        sw2Status = "Released"

def SW3_callback(channel):
    i = 0
    if gpio.input(SW3) == gpio.LOW:
        for client in clients:
            try:
                client.sendall("SW3 pressed, server shutting down...".encode())
            except:
                print(str(client) + "disconnected")
                clients.remove(client)
    while(gpio.input(SW3) == gpio.LOW):
        time.sleep(.1)
        i += .1
        if i >= 3:
            try:
                client.sendall("Server shutting down. Connection terminated.".encode())
            except:
                time.sleep(.1)
            print("Shutting down...")
            os.system("shutdown now -h")
            time.sleep(1)

def clientThread():
    while True:
        status = "{SW1: " + sw1Status + ", SW2: " + sw2Status + "}"
        status = status.encode()
        for client in clients:
            try:
                client.sendall(status)
            except:
                print("Client disconnected")
                clients.remove(client)
        time.sleep(1)

def rLEDThread():
    global rLEDTmr
    while True:
        if rLEDTmr > 0:
            if rLEDTmr == 200:
                gpio.output(rLED, True)
            elif rLEDTmr == 100:
                gpio.output(rLED, False)
            rLEDTmr -= 1
            if rLEDTmr == 0:
                rLEDTmr = 200
        time.sleep(.01)

def gLEDThread():
    global gLEDTmr
    while True:
        if gLEDTmr > 0:
            if gLEDTmr == 100:
                gpio.output(gLED, True)
            elif gLEDTmr == 50:
                gpio.output(gLED, False)
            gLEDTmr -= 1
            if gLEDTmr == 0:
                gLEDTmr = 100
        time.sleep(.01)

gpio.add_event_detect(SW1, gpio.BOTH, callback=SW1_callback, bouncetime=10)
gpio.add_event_detect(SW2, gpio.BOTH, callback=SW2_callback, bouncetime=10)
gpio.add_event_detect(SW3, gpio.BOTH, callback=SW3_callback, bouncetime=10)
#rLEDPWM.start(0)
#gLEDPWM.start(0)

tRLED = threading.Thread(target = rLEDThread)
tRLED.start()
tGLED = threading.Thread(target = gLEDThread)
tGLED.start()

clients = list()

if HOST == "":
    print("Warning, not connected to network. Running in offline mode")
else:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((HOST, PORT))
        #s.bind(("", PORT))
        print("Socket bound")
    except socket.error as message:
        print(message)
    #s.connect(("8.8.8.8", 80))
    print("IP address: " + HOST)
    print("Port: " + str(PORT))
    #print(s)
    s.listen(5)
    #s.close
    t1 = threading.Thread(target = clientThread)
    t1.start()
    print("Connecting to clients...")
    while(True):
        conn, addr = s.accept()
        conn.sendall("Connection successful, sending switch status...".encode())
        print("Connected to " + addr[0] + " on socket " + str(addr[1]))
        #print(conn)
        clients.append(conn)
