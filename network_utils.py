import socket
import subprocess

FORMAT = "utf-8"
PORT = 5555


def dig(*args):
    cmd = ["dig"] + list(*args)
    output = subprocess.check_output(cmd)
    return output.strip().decode()


def dig_get_host_name():
    """Run dig command to find public IP
    Seems to work on both DO ubuntu droplet and adam mac

    If FileNotFoundError -> no dig command found
    If ValueError -> dig command ran but returned empty
    """
    dig_args = ["+short", "myip.opendns.com", "@resolver1.opendns.com"]
    addr = dig(dig_args)

    # i've had cases of cmd running w/o error, but
    # returning blank bytes object, throwing error in this case
    if not addr:
        raise ValueError

    return addr


def get_host_name(default="127.0.0.1"):
    """Try to get host name and fall back to defaults"""
    try:
        return dig_get_host_name()
    except (FileNotFoundError, ValueError):
        pass

    try:
        return socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        pass

    try:
        return socket.gethostbyname(socket.gethostname() + ".local")
    except socket.gaierror:
        pass

    return default


if __name__ == "__main__":
    ip_addr = get_host_name()
    print(f"Best guess for current box's address:\n{ip_addr}")
