from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def load_key():
    """
    Loads the encryption key if it exists.
    Otherwise creates a new key and saves it.
    """

    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)

        print("Encryption key created.")

    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()

    return key


cipher = Fernet(load_key())


def encrypt_message(message):
    """
    Encrypt a plaintext message.
    """

    encrypted = cipher.encrypt(message.encode())

    return encrypted.decode()


def decrypt_message(encrypted_message):
    """
    Decrypt an encrypted message.
    """

    decrypted = cipher.decrypt(encrypted_message.encode())

    return decrypted.decode()
