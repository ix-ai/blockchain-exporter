FROM hub.ix.ai/docker/alpine:latest
LABEL ai.ix.maintainer="docker@ix.ai"

ENV LOGLEVEL=INFO

RUN pip3 install requests

COPY src/blockchain-exporter.py /

EXPOSE 9308

ENTRYPOINT ["python3", "/blockchain-exporter.py"]
