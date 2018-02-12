# -*- coding: utf-8 -*-
import typing as t


class RpcClient:

    def __init__(self, host: str, port: str, user: str, pwd: str, use_ssl: bool=False):
        self.host: str
        self.port: str
        self.user: str
        self.pwd: str
        self.use_ssl: bool

    def _url(self) -> str: ...

    def _call(self, method: str, *args) -> t.Dict: ...

    def _get_methods(self) -> t.List[str]: ...

$methods

