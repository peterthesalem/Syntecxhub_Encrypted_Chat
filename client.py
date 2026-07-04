import socket
from config import HOST, PORT
from encryption import encrypt_message

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

print(f"Connected to {HOST}:{PORT}")

message = "Hello Salem"

encrypted_message = encrypt_message(message)

client.send(encrypted_message.encode())

client.close()
