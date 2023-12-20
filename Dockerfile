FROM alpine
COPY --chmod=700 run.sh /

ENV PORT_LIST="example.com:80 example.com:443"
ENV INTERVAL=60
ENV TIMEOUT=3
ENV NTFY_TOPIC="PortMonitor"

CMD /run.sh
