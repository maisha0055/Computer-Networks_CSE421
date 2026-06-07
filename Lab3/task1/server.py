import socket
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 4949
HEADER = 64
format = 'utf-8'
ADDR = (SERVER, PORT)
Disconnect_msg = 'End'
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(ADDR)
print(f'Server is running on {SERVER}:{PORT}')
SERVER.listen()
print(f'Server is listening on {SERVER}:{PORT}')
while True:
    conn, addr = SERVER.accept()
    print(f'Connection from {addr} has been established.')
    Connected= True
    while Connected:
        msg_length = conn.recv(HEADER).decode(format)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(format)
            if msg == Disconnect_msg:
                Connected = False 
                conn.send('Connection closed'.encode(format))
            else:
                print(f'Message from {addr}: {msg}')
                conn.send('Message received'.encode(format))
    conn.close()