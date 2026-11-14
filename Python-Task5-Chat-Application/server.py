# Chat Server
# Run this first. It accepts many clients and sends each message to everyone else.

import socket
import threading

HOST = "0.0.0.0"
PORT = 5555

clients = []


def send_to_all(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except OSError:
                pass


def handle_client(client):
    # The first message from a client is its name
    name = client.recv(1024).decode()
    client.send("Connected. Type /quit to leave.".encode())
    send_to_all(name + " joined the chat", client)

    while True:
        try:
            message = client.recv(1024).decode()
        except OSError:
            break
        if message == "" or message == "/quit":
            break
        send_to_all(name + ": " + message, client)

    clients.remove(client)
    client.close()
    send_to_all(name + " left the chat", client)
    print(name, "disconnected")


# ---------- Main program ----------
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()
print("Server running on port", PORT)

while True:
    client, address = server.accept()
    print("New connection from", address[0])
    clients.append(client)
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.daemon = True
    thread.start()
