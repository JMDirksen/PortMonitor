#!/bin/sh

if [ -z ${PORT_LIST} ]; then PORT_LIST="example.com:80 example.com:443"; fi
if [ -z ${TIMEOUT} ]; then TIMEOUT=3; fi
if [ -z ${INTERVAL} ]; then INTERVAL=60; fi
if [ -z ${NTFY_TOPIC} ]; then NTFY_TOPIC="PortMonitor"; fi

while true; do
  for port in $PORT_LIST; do
    echo -n "> $port ... "
    nc -zw $TIMEOUT $(echo $port | tr ":" " ")
    if [ $? -eq 0 ]; then
      echo "OK"
    else
      echo "Error"
      curl -s -o /dev/null -d "Error connecting to $port" ntfy.sh/$NTFY_TOPIC
    fi
  done
  sleep $INTERVAL
done
