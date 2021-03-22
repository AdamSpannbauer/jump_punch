import socket
from network_utils import get_host_name, PORT, FORMAT

SERVER = get_host_name()

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((SERVER, PORT))


def respond(data, addr):
    msg = f'you said "{data.decode(FORMAT)}"'
    server.sendto(msg.encode(FORMAT), addr)


def start_server():
    while True:
        data, addr = server.recvfrom(1024)
        print(f"received from: {addr}")
        print(f"received: {data.decode(FORMAT)}")

        respond(data, addr)


if __name__ == "__main__":
    print(f"[STARTING] server is running on {SERVER, PORT}")
    start_server()
