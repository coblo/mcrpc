#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `mcrpc` package."""
import pytest
from string import Template
from decimal import Decimal
from codegen import get_api_methods, get_stub_template
from mcrpc.exceptions import RpcError
from mcrpc import responses


@pytest.fixture
def client():
    import mcrpc
    return mcrpc.autoconnect()


def test_getinfo(client):
    r = client.getinfo()
    assert isinstance(r, responses.Getinfo)


def test_getbalance(client):
    r = client.getbalance()
    assert isinstance(r, Decimal)


def test_nonexisting_method(client):
    with pytest.raises(RpcError):
        client.noexist()


def test_load_stub_template(client):
    assert isinstance(get_stub_template(), Template)


def test_get_api_methods(client):
    methods = get_api_methods(client)
    assert len(methods) == 170


def test_encoding_text(client):
    s = 'I sat döwn for “coffee” at the café'
    try:
        client.create('stream', 'test', True)
    except RpcError:
        pass
    txid = client.publish('test', 'testkey', {'text': s})
    resp = client.getstreamitem('test', txid)
    rs = resp['data']['text']
    assert rs == s

