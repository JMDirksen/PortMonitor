import os
import socket
import requests
import time

PORT_LIST = os.getenv('PORT_LIST') or "example.com:80 example.com:443"
TIMEOUT = int(os.getenv('TIMEOUT')) or 3
INTERVAL = int(os.getenv('INTERVAL')) or 300
INTERVAL_ON_ERROR = int(os.getenv('INTERVAL_ON_ERROR')) or 10
NTFY_TOPIC = os.getenv('NTFY_TOPIC') or "PortMonitor"


def main():
    ports = ports_to_list(PORT_LIST)

    while True:
        errors = False
        for check in ports:
            portString = f"{check['address']}:{check['port']}"
            print(f"> {portString} ... ", end="", flush=True)
            if checkPort(check['address'], check['port']):
                if not check['status']:
                    check['status'] = True
                    send_notification(f"OK: {portString}")
                print("OK", flush=True)
            else:
                errors = True
                if check['status']:
                    check['status'] = False
                    send_notification(f"Error: {portString}")
                print("ERROR", flush=True)
        if errors:
            time.sleep(INTERVAL_ON_ERROR)
        else:
            time.sleep(INTERVAL)


def send_notification(message: str):
    try:
        requests.post(
            f"https://ntfy.sh/{NTFY_TOPIC}", data=message)
    except Exception as e:
        print(e, end=" ")


def ports_to_list(ports: str) -> list:
    portsList = []
    for portString in ports.split():
        address, port = portString.split(':')
        portsList.append(
            {'address': address, 'port': int(port), 'status': True}
        )
    return portsList


def checkPort(address: str, port: int):
    try:
        s = socket.socket()
        s.settimeout(TIMEOUT)
        s.connect((address, port))
    except Exception as e:
        return False
    finally:
        s.close()
    return True


if __name__ == "__main__":
    main()
