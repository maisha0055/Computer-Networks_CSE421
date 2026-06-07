import socket

SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 4949
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'
HEADER = 64
DISCONNECT_MSG = "End"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

print(f"Server running on {SERVER_IP}:{PORT}")
server.listen()
print("Server is listening...")

while True:
    conn, addr = server.accept()
    print(f"Connected with {addr}")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MSG:
                connected = False
                conn.send("Connection closed".encode(FORMAT))
            else:
                try:
                    hours = float(msg)

                    if hours <= 40:
                        salary = hours * 200
                    else:
                        extra_hours = hours - 40
                        salary = 8000 + (extra_hours * 300)

                    result = f"Salary = Tk {salary}"
                except:
                    result = "Invalid input. Please send a number."

                conn.send(result.encode(FORMAT))

    conn.close()