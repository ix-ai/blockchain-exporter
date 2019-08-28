FROM alpine:latest
LABEL maintainer="docker@ix.ai"

ARG PORT=9308
ARG LOGLEVEL=INFO

RUN apk --no-cache upgrade && \
    apk --no-cache add python3 gcc musl-dev && \
    pip3 install --no-cache-dir prometheus_client pygelf requests

ENV LOGLEVEL=${LOGLEVEL} PORT=${PORT}

COPY src/blockchain-exporter.py /

EXPOSE ${PORT}

ENTRYPOINT ["python3", "/blockchain-exporter.py"]
