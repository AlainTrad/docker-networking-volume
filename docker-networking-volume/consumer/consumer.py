import socket

HOST = "producer"  # The hostname of the producer container
PORT = 5000
FILE_PATH = "/data/logs.txt"

# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print(f"Connected to {HOST}:{PORT}")

with open(FILE_PATH, "a") as file:
    while True:
        data = client.recv(1024).decode().strip()
        if not data:
            break
        print(f"Received: {data}")
        file.write(data + "\n")
        file.flush()
