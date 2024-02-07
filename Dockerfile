FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT_LIST="example.com:80 example.com:443"
ENV INTERVAL=300
ENV INTERVAL_ON_ERROR=10
ENV TIMEOUT=3
ENV NTFY_TOPIC="PortMonitor"

CMD [ "python", "./run.py" ]
