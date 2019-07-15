# blockchain-exporter

A Bitcoin exporter using the [blockchain.com/explorer](https://www.blockchain.com/explorer) API, for [Prometheus](https://prometheus.io)

## Usage
```
docker run --rm -it -p 9399:9399 \
  -e LOGLEVEL=DEBUG \
  -e PORT=9399 \
  --name blockchain-exporter \
  hub.ix.ai/docker/blockchain-exporter:latest
```

## Supported variables
* `ACCOUNTS` (no default) - comma separated list of the accounts monitor the balances
* `URL` (default `https://blockchain.info`) - the API base URL
* `GELF_HOST` (no default) - if set, the exporter will also log to this [GELF](https://docs.graylog.org/en/3.0/pages/gelf.html) capable host on UDP
* `GELF_PORT` (defaults to `12201`) - the port to use for GELF logging
* `PORT` (defaults to `9308`) - the listen port for the exporter
* `LOGLEVEL` (defaults to `INFO`)
