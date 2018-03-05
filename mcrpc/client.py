# -*- coding: utf-8 -*-
"""Multichain RPC Client"""
import simplejson as json
import requests
from functools import partial
from decimal import Decimal
from mcrpc.exceptions import RpcError
from mcrpc.base import BaseApiMethods


class RpcClient(BaseApiMethods):

    def __init__(self, host, port, user, pwd, use_ssl=False):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.use_ssl = use_ssl

    @property
    def _url(self):
        url = '{}:{}@{}:{}'.format(self.user, self.pwd, self.host, self.port)
        return 'https://' + url if self.use_ssl else 'http://' + url

    def _call(self, method, *args):
        args = [arg for arg in args if arg is not None]
        payload = {"method": method, "params": args}
        serialized = json.dumps(payload, use_decimal=True)
        response = requests.post(self._url, data=serialized, verify=False)
        data = response.json(parse_float=Decimal)
        if data['error'] is not None:
            raise RpcError(data['error'].get('message'))
        return data['result']

    def __getattr__(self, method):
        return partial(self._call, method)


if __name__ == '__main__':
    c = RpcClient('127.0.0.1', '7010', 'testuser', 'testpassword', False)
