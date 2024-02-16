import socket

HOST = "127.0.0.1"  # IP address of your Elixir server
PORT = 65432  # Port the Elixir server is listening on


def test_connection():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Test data to send (adjust as needed)
        data = b"Hello from Python!\n"
        s.sendall(data)

        # Receive response (replace 1024 with appropriate buffer size)
        response = s.recv(1024)
        print(f"Received from Elixir server: {response.decode('utf-8')}")


if __name__ == "__main__":
    test_connection()
