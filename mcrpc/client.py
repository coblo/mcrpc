# -*- coding: utf-8 -*-
"""Multichain RPC Client"""
import json
import requests
from functools import partial

from mcrpc.exceptions import RpcError


class RpcClient:

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
        serialized = json.dumps(payload)
        response = requests.post(self._url, data=serialized, verify=False)
        data = response.json()
        if data['error'] is not None:
            raise RpcError(data['error'].get('message'))
        return data['result']

    def __getattr__(self, item):
        return partial(self._call, item)


if __name__ == '__main__':
    c = RpcClient('127.0.0.1', '7010', 'testuser', 'testpassword', False)
    assert isinstance(c.getinfo(), dict)




