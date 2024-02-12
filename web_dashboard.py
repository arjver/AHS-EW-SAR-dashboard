"""
Send stuff to the web dashboard.

Example:
```
import web_dashboard as wd

wd.id = "<your id>"
wd.init_grid(10)
wd.init_log()
wd.set_square(0, 0, "red")
wd.log("Hello, world!")
```
"""

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


def init_log():
    message = f"initlog/{id}".encode()
    sock.sendall(message)

    data = sock.recv(1024)
    # TODO error handle


def log(msg: str):
    message = f"log/{id}/{msg}".encode()
    sock.sendall(message)

    data = sock.recv(1024)
    # TODO error handle
