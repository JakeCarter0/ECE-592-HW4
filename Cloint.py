import socket
import sys
from time import sleep
"""
Created: 7/12/2022
Purpose: to act as the client file for receiving data from the pi.
"""

#get information from command line
s = socket.socket()
if sys.argv[1:] and sys.argv[2:]:
    host = sys.argv[1]
    try:
        port = int(sys.argv[2])
    except:
        print('Use a number for port. Suggest using 8888.')
        sys.exit()
else:
    print("Please input argument IP for the server and or the port")
    sys.exit()

#try to connect to the server pi
try:
    s.connect((host,port))
except:
    print('Timeout occured')
    sys.exit()

print(s.recv(1024))

#continually prints data
while True:
    data = s.recv(1024)
    #print(s.recv(1024))
    if data == b'':     #quits the program if the connection is severed
        print('Server not available')
        sys.exit()
    print(data)

