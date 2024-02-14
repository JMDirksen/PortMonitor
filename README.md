# PortMonitor
 
Docker container checking if ports are accepting connections, if not it will send a push notification through [Ntfy.sh](https://ntfy.sh/)


# Environment variables

Variable | Default value | Description
--|--|--
PORT_LIST | example.com:80 example.com:443 | A space delimited list of host:port strings
INTERVAL | 300 | The interval in seconds before testing the ports again
INTERVAL_ON_ERROR | 10 | The interval in seconds before testing the ports again when there has been an error during last checks
TIMEOUT | 3 | Number of seconds to wait for a connection to be made
NOTIFY_ERROR_COUNT | 2 | Number of failed attempts to connect to the port before sending a notification
NTFY_TOPIC | PortMonitor | The [ntfy topic](https://docs.ntfy.sh/?h=topic#step-1-get-the-app) to send the push notifications to
