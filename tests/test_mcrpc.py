#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `mcrpc` package."""
import unittest
from string import Template
from decimal import Decimal
from codegen import get_api_methods, get_stub_template
from mcrpc import RpcClient
from mcrpc.exceptions import RpcError
from mcrpc import responses


class TestMCRPC(unittest.TestCase):
    """Tests for `mcrpc` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.c = RpcClient(
            '127.0.0.1', '9000', 'testuser', 'testpassword', False
        )

    def test_getinfo(self):
        r = self.c.getinfo()
        self.assertIsInstance(r, responses.Getinfo)

    def test_getbalance(self):
        r = self.c.getbalance()
        self.assertIsInstance(r, Decimal)

    def test_nonexisting_method(self):
        with self.assertRaises(RpcError):
            self.c.noexist()

    def test_load_stub_template(self):
        self.assertIsInstance(get_stub_template(), Template)

    def test_get_api_methods(self):
        methods = get_api_methods(self.c)
        self.assertEqual(len(methods), 170)
        self.c.getinfo()

    def test_encoding_text(self):
        s = 'I sat döwn for “coffee” at the café'
        try:
            self.c.create('stream', 'test', True)
        except RpcError:
            pass
        txid = self.c.publish('test', 'testkey', {'text': s})
        resp = self.c.getstreamitem('test', txid)
        rs = resp['data']['text']
        self.assertEqual(rs, s)
