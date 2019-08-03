FROM registry.gitlab.com/ix.ai/alpine:latest
LABEL MAINTAINER="docker@ix.ai"

ARG PORT

ENV LOGLEVEL=INFO PORT=${PORT}

RUN pip3 install --no-cache-dir requests

COPY src/blockchain-exporter.py /

EXPOSE ${PORT}

ENTRYPOINT ["python3", "/blockchain-exporter.py"]
