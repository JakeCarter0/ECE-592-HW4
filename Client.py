"""
Created on July 10 2022

@author:
PiE Homework 4
Client program designed to receive switch states from LEDServer.py every second.
This code takes 2 arguments, the first being the IP address of the server raspberry pi, and the second being the port number. These will be displayed by the server program.
EX: "python Client.py 192.168.1.25 3454"
"""


import socket
import sys

s = socket.socket()
if sys.argv[1:]:
    HOST = sys.argv[1]# ip of raspberry pi
else:
    print("Please input argument IP for the server")
    sys.exit()

if sys.argv[2:]:
    PORT = sys.argv[2]# ip of raspberry pi
else:
    print("Please input argument Port for the server")
    sys.exit()
#print(HOST)
#print(PORT)
s.settimeout(5)
try:
    s.connect((HOST, int(PORT)))
except (ConnectionRefusedError, TimeoutError):
    print("Server not found. Exiting program...")
    sys.exit()
print(s.recv(1024).decode())
while True:
    msg = s.recv(1024).decode()
    if msg != "":
        print(msg)
    else:
        print("Connection lost. Exiting program...")
        break
sys.exit()
