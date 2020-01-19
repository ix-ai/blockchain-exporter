FROM alpine:latest
LABEL maintainer="docker@ix.ai"

WORKDIR /app

COPY src/ /app

RUN apk --no-cache upgrade && \
    apk --no-cache add python3 gcc musl-dev && \
    pip3 install --no-cache-dir -r requirements.txt && \
    apk del --no-cache --purge gcc musl-dev

EXPOSE 9308

ENTRYPOINT ["python3", "/app/blockchain-exporter.py"]
