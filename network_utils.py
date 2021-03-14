import socket

FORMAT = "utf-8"
PORT = 5555


def get_host_name(default="127.0.0.1"):
    """Try to get host name and fall back to defaults"""
    try:
        return socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        try:
            return socket.gethostbyname(socket.gethostname() + ".local")
        except socket.gaierror:
            return default
