#!/bin/bash

timeout=3
port_list="example.com:80 example.com:443"
ntfy_topic="PortMonitor"

for port in $port_list; do
  echo -n "> $port ... "
  nc -zw $timeout $(echo $port | tr ":" " ")
  [[ $? -eq 0 ]] && echo "OK" || (echo "Error"; curl -s -o /dev/null -d "Error connecting to $port" ntfy.sh/$ntfy_topic)
done
