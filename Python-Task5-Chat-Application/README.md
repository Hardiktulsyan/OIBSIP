# Chat Application (Python Programming, Task 5)

A simple chat room using sockets. One server, many clients. Messages from one client are shown to all the others.

## Features
- Many clients can join at the same time
- Join and leave messages
- Type /quit to leave
- Shows an error if the server is not running

## Requirements
Python 3, no extra packages.

## How to run
Open separate terminals.
1. `python server.py`
2. `python client.py` (run this in two or more terminals)

To chat from another computer on the same network, change SERVER_IP in client.py to the server computer's IP address.

## Files
- server.py : accepts clients and passes messages to everyone else
- client.py : sends your messages and prints the ones you receive
