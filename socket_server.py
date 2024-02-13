import socket
import requests
import threading

web_server_url = "http://localhost:3010"
port = 3020


def handle_client(client_socket):
    print("client connected")

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            msg = data.decode()
            print(msg)
            requests.get(web_server_url + "/" + msg)
            # client_socket.sendall(bytes(requests.get(web_server_url + "/" + msg).text, "utf-8"))
        except Exception as e:
            print(e)
            break

    print("client disconnected")
    client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("0.0.0.0", 3020)
server_socket.bind(server_address)

print(f"listening on port {port}")

server_socket.listen(1)

while True:
    try:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
    except KeyboardInterrupt:
        break

server_socket.close()
