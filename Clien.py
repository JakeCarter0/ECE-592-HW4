# -*- coding: utf-8 -*-
"""
Client will receive data from Raspberrypi for HW4
"""

#client setup code uses class code examples as reference
import socket
import sys
import time
s = socket.socket()
s.close()
s = socket.socket()
t=0
if len(sys.argv)==3:
    IP = sys.argv[1]
    port = int(sys.argv[2])
# IP = '192.168.137.32'
# port = 8888
else:
    print("IP Address and port for server (raspberrypi) arguments needed")
    sys.exit(0)
print('Attempting to connect..')
while True:
    try:
        s.connect((IP, port))
        print('Connected to server.\n')
        break
    except(ConnectionRefusedError):
        print('Trying to connect..')
        #gives 4 seconds to try to connect to server
        time.sleep(1)
        t += 1
        if t>3:
            print('Server connection refused. Client exiting')
            sys.exit(0)
    except(TimeoutError):
        print('Unable to connect to server. Timeout Error.')
        sys.exit(0)
while(True):
    try:
        servermsg = s.recv(1024)
        if servermsg == b'q' or servermsg == b'':
            print('Server has closed. Client is quitting..')
            s.close()
            sys.exit(0)
        else:
            print(servermsg)
    except(socket.error):
        print('Server has closed. Client is quitting..')
        s.close()
        sys.exit(0)
