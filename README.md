# blockchain-exporter

[![Pipeline Status](https://gitlab.com/ix.ai/blockchain-exporter/badges/master/pipeline.svg)](https://gitlab.com/ix.ai/blockchain-exporter/)
[![Docker Stars](https://img.shields.io/docker/stars/ixdotai/blockchain-exporter.svg)](https://hub.docker.com/r/ixdotai/blockchain-exporter/)
[![Docker Pulls](https://img.shields.io/docker/pulls/ixdotai/blockchain-exporter.svg)](https://hub.docker.com/r/ixdotai/blockchain-exporter/)
[![Gitlab Project](https://img.shields.io/badge/GitLab-Project-554488.svg)](https://gitlab.com/ix.ai/blockchain-exporter/)

A Bitcoin exporter using the [blockchain.com/explorer](https://www.blockchain.com/explorer) API, for [Prometheus](https://prometheus.io)

## Usage
```
docker run --rm -it -p 9399:9399 \
  -e LOGLEVEL=DEBUG \
  -e PORT=9399 \
  --name blockchain-exporter \
  registry.gitlab.com/ix.ai/blockchain-exporter:latest
```
Or use the image from `ixdotai/blockchain-exporter`

```
docker run --rm -it -p 9399:9399 \
  -e LOGLEVEL=DEBUG \
  -e PORT=9399 \
  --name blockchain-exporter \
  ixdotai/blockchain-exporter:latest
```

## Supported variables
* `ACCOUNTS` (no default - **mandatory**) - comma separated list of the accounts monitor the balances
* `URL` (default `https://blockchain.info`) - the API base URL
* `GELF_HOST` (no default) - if set, the exporter will also log to this [GELF](https://docs.graylog.org/en/3.0/pages/gelf.html) capable host on UDP
* `GELF_PORT` (defaults to `12201`) - the port to use for GELF logging
* `PORT` (defaults to `9308`) - the listen port for the exporter
* `LOGLEVEL` (defaults to `INFO`)

## Tags and Arch

Starting with version v0.4.0, the images are multi-arch, with builds for amd64, arm64 and armv7.
* `vN.N.N` - for example v0.4.0
* `latest` - always pointing to the latest version
* `dev-branch` - the last build on a feature/development branch
* `dev-master` - the last build on the master branch

## Resources:
* GitLab: https://gitlab.com/ix.ai/blockchain-exporter
* GitLab: https://github.com/ix-ai/blockchain-exporter
* Docker Hub: https://hub.docker.com/r/ixdotai/blockchain-exporter
