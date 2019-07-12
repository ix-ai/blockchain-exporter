# blockchain-exporter

A Bitcoin exporter using the [blockchain.com/explorer](https://www.blockchain.com/explorer) API, for [Prometheus](https://prometheus.io)

## Usage
```
docker run --rm -it -p 9308:9308 \
  -e LOGLEVEL=DEBUG \
  --name blockchain-exporter \
  hub.ix.ai/docker/blockchain-exporter:latest
```

## Supported variables
* `ACCOUNTS` (no default) - comma separated list of the accounts monitor the balances
* `URL` (default `https://blockchain.info`) - the API base URL
* `LOGLEVEL` (defaults to `INFO`)
