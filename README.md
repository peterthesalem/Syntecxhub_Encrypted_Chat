# 🔐 Encrypted Chat Application

A simple encrypted chat application built in Python using TCP sockets and the `cryptography` (Fernet) library.

## 📌 Project Overview

This project was completed as part of the **SyntecxHub Cybersecurity Internship**.

It demonstrates how secure communication can be achieved by combining socket programming with symmetric encryption.

## ✨ Features

- TCP client-server communication
- Message encryption and decryption
- Automatic encryption key generation
- Secure message transmission
- Simple and modular project structure

## 🛠 Technologies Used

- Python 3
- Socket Programming
- Cryptography (Fernet)

## 📂 Project Structure

```
Syntecxhub_Encrypted_Chat/
│── client.py
│── server.py
│── encryption.py
│── config.py
│── requirements.txt
│── README.md
│── .gitignore
```

## 🚀 Installation

```bash
pip install -r requirements.txt
```

## ▶️ Run the Server

```bash
python3 server.py
```

## ▶️ Run the Client

```bash
python3 client.py
```

## 📸 Sample Output

Server

```
Server listening on 127.0.0.1:5000
Client connected from ('127.0.0.1', 60990)
Encrypted: gAAAAAB...
Decrypted: Hello Salem
```

Client

```
Connected to 127.0.0.1:5000
```

## 👨‍💻 Author

**Olayinka Akoshile**

Project completed during the **SyntecxHub Cybersecurity Internship**.
