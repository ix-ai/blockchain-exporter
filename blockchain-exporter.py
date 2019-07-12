#!/usr/bin/env python3
"""A Bitcoin exporter using the blockchain.com/explorer API, for Prometheus"""

import logging
import time
import os
import sys
import requests
from prometheus_client import start_http_server
from prometheus_client.core import REGISTRY, GaugeMetricFamily

LOG = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=os.environ.get("LOGLEVEL", "INFO"),
    format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


class BlockchainCollector:
    """ The BlockchainCollector class """
    accounts = {}

    def __init__(self):
        self.settings = {
            'addresses': os.environ.get("ADDRESSES", '').split(','),
            'url': os.environ.get('URL', 'https://blockchain.info'),
        }

    def get_balance(self):
        """ Connects to the blockchain API and retrieves the account information """
        if not self.settings['addresses']:
            return
        addresses = '|'.join(self.settings['addresses'])
        url = '{}/balance'.format(
            self.settings['url']
        )
        request_data = {
            'active': addresses,
        }
        LOG.debug('URL: {}'.format(url))
        LOG.debug('request_data: {}'.format(request_data))

        try:
            r = requests.get(url, params=request_data).json()
            LOG.debug('Response: {}'.format(r))
        except (
                requests.exceptions.ConnectionError,
                requests.exceptions.ReadTimeout
        ) as e:
            LOG.warning("Can't connect to {}. The error received follows.".format(
                self.settings['url']
            ))
            LOG.warning(e)

        for address in self.settings['addresses']:
            if r.get(address):
                currency = 'BTC'
                balance = float(int(r.get(address).get('final_balance')) / 100000000)
                LOG.debug('Registering balance {balance} for the account {account} {currency}'.format(
                    balance=balance,
                    currency=currency,
                    account=address
                ))
                self.accounts.update({
                    address: {
                        'value': balance,
                        'currency': currency,
                        'type': 'blockchain',
                    }
                })
            else:
                LOG.warning('Could not retrieve balance. The result follows.')
                LOG.warning('{}: {}'.format(r.get('result'), r.get('message')))

    def describe(self):
        """ Just a needed method, so that collect() isn't called at startup """
        return []

    def collect(self):
        """ The actual collector """
        metrics = {
            'account_balance': GaugeMetricFamily(
                'account_balance',
                'Account Balance',
                labels=['source_currency', 'currency', 'account', 'type']
            ),
        }
        self.get_balance()
        for account in self.accounts:
            metrics['account_balance'].add_metric(
                value=self.accounts[account]['value'],
                labels=[
                    self.accounts[account]['currency'],
                    self.accounts[account]['currency'],
                    account,
                    self.accounts[account]['type']
                ]
            )

        for metric in metrics.values():
            yield metric


if __name__ == '__main__':
    LOG.info("Starting")
    REGISTRY.register(BlockchainCollector())
    start_http_server(9308)
    while True:
        time.sleep(1)
