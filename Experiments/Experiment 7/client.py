import socket

# Client Configuration
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  # Make sure it matches the server's IP
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 64
DISCONNECT_MESSAGE = '!DISCONNECT'

# Create Client Socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Function to Send Messages
def send(messages):
    message = messages.encode(FORMAT)
    messageLength = str(len(message)).encode(FORMAT)
    messageLength = messageLength.ljust(HEADER)  # Ensure it's exactly HEADER bytes
    client.send(messageLength)
    client.send(message)
    print(client.recv(HEADER).decode(FORMAT))

# Run Client Interaction
if __name__ == '__main__':
    while True:
        msg = input("Enter message (or type '!DISCONNECT' to exit): ")
        send(msg)
        if msg == DISCONNECT_MESSAGE:
            break
