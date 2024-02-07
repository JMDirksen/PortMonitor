import os, socket

PORT_LIST = os.getenv('PORT_LIST') or "example.com:80 example.com:443"
TIMEOUT = os.getenv('TIMEOUT') or 3
INTERVAL = os.getenv('INTERVAL') or 60
NTFY_TOPIC = os.getenv('NTFY_TOPIC') or "PortMonitor"


def main():
    print(checkPort("example.com:80"))


def checkPort(port):
    try:
        address, port = port.split(':')
        s = socket.socket()
        s.settimeout(TIMEOUT)
        s.connect((address, int(port)))
    except Exception as e:
        return False
    finally:
        s.close()
    return True


if __name__ == "__main__":
    main()
