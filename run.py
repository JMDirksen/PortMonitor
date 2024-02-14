import os
import socket
import requests
import time

# Get/set environment variables / defaults
PORT_LIST = os.getenv('PORT_LIST') or "example.com:80 example.com:443"
INTERVAL = int(os.getenv('INTERVAL') or 300)
NOTIFY_ERROR_COUNT = int(os.getenv('NOTIFY_ERROR_COUNT') or 2)
TIMEOUT = int(os.getenv('TIMEOUT') or 3)
NTFY_TOPIC = os.getenv('NTFY_TOPIC') or "PortMonitor"


def main():
    ports = ports_to_list(PORT_LIST)

    while True:
        for port in ports:
            print(f"> {port['string']} ... ", end="", flush=True)
            # Check port
            if checkPort(port['address'], port['port']):
                # OK
                print("OK", flush=True)
                if port['error_count'] >= NOTIFY_ERROR_COUNT:
                    # Notify back from Error to OK
                    send_notification("OK", port['string'])
                port['error_count'] = 0
            else:
                # Error
                port['error_count'] += 1
                print(f"ERROR {port['error_count']}", flush=True)
                if port['error_count'] == NOTIFY_ERROR_COUNT:
                    # Notify Error
                    send_notification("Error", port['string'], True)
        time.sleep(INTERVAL)


def send_notification(title: str, message: str, warning: bool = False):
    prio = "3"
    tag = "+1"
    if warning:
        prio = "5"
        tag = "warning"
    try:
        requests.post(
            f"https://ntfy.sh/{NTFY_TOPIC}",
            data=message,
            headers={"Title": title, "Priority": prio, "Tags": tag}
        )
        print("Notification sent", flush=True)
    except Exception as e:
        print(e, end=" ")


def ports_to_list(ports: str) -> list:
    portsList = []
    for portString in ports.split():
        address, port = portString.split(':')
        portsList.append(
            {'string': portString, 'address': address,
                'port': int(port), 'error_count': 0}
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
