import socket

HOST = "127.0.0.1"
PORT = 3101

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = b"set/hi2/1/1/green"
    s.sendall(data)
