# import socket

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server_address = ('0.0.0.0', 3020)
# sock.connect(server_address)

# while ...:
#     message = b'set/test/0/0/green'
#     sock.sendall(message)

#     data = sock.recv(1024)
#     print('Received data:', data.decode())

import socket

SERVER_ADDRESS = ("0.0.0.0", 3020)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(SERVER_ADDRESS)

id = ""

# ("red" | "green" | "blue" | "yellow" | "cyan" | "magenta" | "none" | "magnet" | "grey")


def set_square(x: int, y: int, color: str):
    if color not in [
        "red",
        "green",
        "blue",
        "yellow",
        "cyan",
        "magenta",
        "none",
        "magnet",
        "grey",
    ]:
        raise ValueError("Invalid color")

    message = f"set/{id}/{x}/{y}/{color}".encode()
    sock.sendall(message)

    data = sock.recv(1024)
    # TODO error handle


def init_grid(grid_size: int):
    message = f"init/{id}/{grid_size}/{grid_size}".encode()
    sock.sendall(message)

    data = sock.recv(1024)
    # TODO error handle


id = "test1"
init_grid(10)
set_square(0, 0, "red")
set_square(0, 1, "green")
