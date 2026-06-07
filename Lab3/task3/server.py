import socket
import threading
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

def handle_client(conn, addr):
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
                vowels= 'aeiouAEIOU'
                count = 0
                for char in msg:
                    if char in vowels:
                        count += 1
                if count == 0:
                    conn.send('Not enough vowels'.encode(format))
                elif count <= 2:
                    conn.send('Enough vowels I guess'.encode(format))
                else:
                    conn.send('Too many vowels'.encode(format))
    conn.close()
    
while True:
    conn, addr = SERVER.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()