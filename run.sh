#!/bin/sh

while :
do
  for port in $PORT_LIST
  do
    echo -n "> $port ... "
    nc -zw $TIMEOUT $(echo $port | tr ":" " ")
    if [ $? -eq 0 ]
    then
      echo "OK"
    else
      echo "Error"
      curl -s -o /dev/null -d "Error connecting to $port" ntfy.sh/$NTFY_TOPIC
    fi
  done
  sleep $INTERVAL
done
