import socket
import time
import random

HOST = "0.0.0.0"  # Listen on all available network interfaces
PORT = 5000

messages = ["Hello", "Docker Networking", "Random Data", "Test Log", "Python Server"]

# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Producer is listening on port {PORT}...")

conn, addr = server.accept()
print(f"Connection from {addr} established!")

while True:
    message = random.choice(messages)
    conn.sendall(f"{message}\n".encode())
    print(f"Sent: {message}")
    time.sleep(2)  # Send data every 2 seconds
