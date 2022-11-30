"""
Reference material for this assignment includes the lectures and code related to socket client programming provided on the ECE592 moodle website, along socket and python documentation:

https://docs.python.org/3/howto/sockets.html
https://docs.python.org/3/library/
"""
try:
    import socket
    import sys
    from time import time
except:
    print("**ERROR** You need the following libraries installed to run this program")
    print("socket")
    print("sys")
    print("time")
CLOSE_CONNECTION = 'SW3 pressed, server shutting down..'

def decode_text_from_server(socket):
    """function to decode the message from the server"""
    message = socket.recv(79)#the strings we're expecting to receive are atleast 79 bytes
    if not message:#make sure we got a valid message
        print('Invalid message received')
        return None

    decoded_message = message.decode('utf-8')#decode the incomming message
    return decoded_message

def valid_number(number):
    """function to check for a valid number adapted from previous assignments"""
    try:
        int_phone_num = int(number) #see if we can cast it to type int
        return True
    except:#otherwise false
        return False
        
def main():
    """main function to set up server and receive messages"""
    s = socket.socket()        
    if len(sys.argv[1:]) == 2:
        host = sys.argv[1]# ip of raspberry pi
        port = sys.argv[2]#port
    else:
        print("Please input 2 arguments, IP and port for the server")
        print("The ip address and port number are printed in the raspberry pi python console when the server is up and running")
        print("The program should be run by typing 'python Client.py <provided ip address> <provided port number>'")
        print('Trying with default ip = "192.168.0.162" and port # = "8888"')
        host = "192.168.0.162"
        port = "8888"
        #sys.exit()         

    if not valid_number(port):#make sure port # is valid integer
        print("port is not a valid number.. try again")
        sys.exit()

    connected = False
    t0 = time()
    while not connected:
        try:
            s.connect((host, int(port)))    # try to connect to the host
            print('socket connected')
            connected = True
        except:#otherwise wait 5 sections and then timeout if necessary
            if time()-t0 > 5: 
                print("Server not available")
                print("Could not connect to server after 5 seconds, exiting....")
                sys.exit()    
    while(True):
        rx_data = decode_text_from_server(s)#decode the text from the server
        if rx_data == None:#if we get an invalid message the server disconnected 
            print("Server Disconnected")
            print("Closing Connection..")
            s.close()#close connection
            sys.exit()#exit the program
        else:
            print(rx_data)
        if rx_data == CLOSE_CONNECTION:#if we get the message that the connection is going to be closed. exit the program
            print("Closing Connection..")
            s.close()
            sys.exit()

if __name__ == "__main__":
    main()