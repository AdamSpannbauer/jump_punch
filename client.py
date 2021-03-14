import socket
from network_utils import get_host_name, PORT, FORMAT

SERVER = get_host_name()

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("test1".encode(FORMAT), (SERVER, PORT))
data, addr = client.recvfrom(1024)

print(f"response from: {addr}")
print(f"received: {data.decode(FORMAT)}")
