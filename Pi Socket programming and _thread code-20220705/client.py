import socket
import sys
from time import sleep

s = socket.socket()        
if sys.argv[1:]:
    host = sys.argv[1]# ip of raspberry pi
else:
    print("Please input argument IP for the server")
    sys.exit()         

s.connect((host, 8888))
print(s.recv(1024))
#s.close()
while(True):
    data = input("Type message to end and e to close connection: ")
    if data in ('e', 'E'):
            s.close()
            break
    else:
        data = data.encode()
        s.sendall(data)
        #sleep(0.5)
        print(s.recv(1024))

