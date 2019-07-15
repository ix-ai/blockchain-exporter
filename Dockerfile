FROM hub.ix.ai/docker/alpine:latest
LABEL ai.ix.maintainer="docker@ix.ai"
ARG PORT

ENV LOGLEVEL=INFO PORT=${PORT}

RUN pip3 install --no-cache-dir requests

COPY src/blockchain-exporter.py /

EXPOSE ${PORT}

ENTRYPOINT ["python3", "/blockchain-exporter.py"]
