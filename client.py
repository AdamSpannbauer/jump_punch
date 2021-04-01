import socket
from network_utils import get_host_name, PORT, FORMAT

SERVER = get_host_name()


class Client:
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, data):
        self.connection.sendto(data.encode(FORMAT), (SERVER, PORT))

    def recv(self):
        data, addr = self.connection.recvfrom(1024)

        print(f"response from: {addr}")
        print(f"received: {data.decode(FORMAT)}")


if __name__ == "__main__":
    client = Client(SERVER, PORT)
    client.send("whats up")
    client.recv()
