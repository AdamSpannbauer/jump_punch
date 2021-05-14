import socket
import network_utils as utils
from network_utils import PORT, FORMAT

SERVER = utils.get_host_name()

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((SERVER, PORT))

PLAYER_DATA = {}


def respond(data, addr):
    player_id, x, y = utils.decode_network_data(data)

    print(f"Player {player_id} is at position {x}, {y}")
    PLAYER_DATA[player_id] = {
        "data": utils.encode_network_data(player_id, x, y),
        "x": x,
        "y": y,
    }

    # TODO: how to keep track of opponent? receive id?
    # Find a player id that's not the one just received
    pids = PLAYER_DATA.keys()

    try:
        other_player_id = [pid for pid in pids if pid != player_id][0]
        msg = PLAYER_DATA[other_player_id]["data"]
    except IndexError:
        msg = "No opponent".encode(FORMAT)

    server.sendto(msg, addr)


def start_server():
    while True:
        data, addr = server.recvfrom(1024)
        print(f"received from: {addr}")
        print(f"received: {data.decode(FORMAT)}")

        respond(data, addr)


if __name__ == "__main__":
    print(f"[STARTING] server is running on {SERVER, PORT}")
    start_server()
