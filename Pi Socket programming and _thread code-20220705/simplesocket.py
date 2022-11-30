import socket

HOST = "10.155.25.105"  # Standard loopback interface address (localhost)
PORT = 8888        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            conn.sendall(b'Thanks for connecting')
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            s.close()