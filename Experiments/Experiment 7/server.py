import socket
import threading

# Server Configuration
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  # Get local machine IP
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 64
DISCONNECT_MESSAGE = '!DISCONNECT'

# Create and Bind Server Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Client Handling Function
def clientHandling(connection, address):
    print(f'[NEW CONNECTION] {address} connected')
    isConnected = True
    while isConnected:
        messageLength = connection.recv(HEADER).decode(FORMAT)
        if messageLength:
            messageLength = int(messageLength)
            message = connection.recv(messageLength).decode(FORMAT)
            if message == DISCONNECT_MESSAGE:
                isConnected = False
            print(f'[{address}] {message}')
            connection.send('Message Received'.encode(FORMAT))
    connection.close()

# Start Server
def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=clientHandling, args=(connection, address))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')

print('[SERVER STARTING] Server has been started')
start()
