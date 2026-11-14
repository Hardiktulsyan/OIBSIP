# Chat Client
# Run this after the server. Start it in as many terminals as you like.

import socket
import threading

SERVER_IP = "127.0.0.1"
PORT = 5555


def receive_messages(connection):
    # Runs in the background and prints every message from the server
    while True:
        try:
            message = connection.recv(1024).decode()
        except OSError:
            break
        if message == "":
            print("Disconnected from server.")
            break
        print(message)


# ---------- Main program ----------
name = input("Enter your name: ").strip()

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connection.connect((SERVER_IP, PORT))
except OSError:
    print("Could not connect. Is the server running?")
    exit()

connection.send(name.encode())
print(connection.recv(1024).decode())

thread = threading.Thread(target=receive_messages, args=(connection,))
thread.daemon = True
thread.start()

while True:
    message = input()
    connection.send(message.encode())
    if message == "/quit":
        break

connection.close()
