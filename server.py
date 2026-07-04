import socket
from config import HOST, PORT
from encryption import decrypt_message

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

print(f"Server listening on {HOST}:{PORT}")

client, address = server.accept()

print(f"Client connected from {address}")

encrypted_message = client.recv(1024).decode()

print("Encrypted:", encrypted_message)

decrypted_message = decrypt_message(encrypted_message)

print("Decrypted:", decrypted_message)

client.close()
server.close()
