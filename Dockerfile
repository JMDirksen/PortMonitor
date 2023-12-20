FROM alpine
RUN apk update && apk add --no-cache curl
COPY --chmod=700 run.sh /

ENV PORT_LIST="example.com:80 example.com:443"
ENV INTERVAL=300
ENV TIMEOUT=3
ENV NTFY_TOPIC="PortMonitor"

CMD /run.sh
