import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('0.0.0.0', 3020)
sock.connect(server_address)

while ...:
    message = b'set/test/0/0/green'
    sock.sendall(message)

    data = sock.recv(1024)
    print('Received data:', data.decode())