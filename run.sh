#!/bin/sh

while :
do
  for port in $PORT_LIST; do
    echo -n "> $port ... "
    nc -zw $TIMEOUT $(echo $port | tr ":" " ")
    [[ $? -eq 0 ]] && echo "OK" || (echo "Error"; curl -s -o /dev/null -d "Error connecting to $port" ntfy.sh/$NTFY_TOPIC)
  done
  sleep $INTERVAL
done
