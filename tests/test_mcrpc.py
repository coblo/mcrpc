#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `mcrpc` package."""
import unittest
from mcrpc import RpcClient
from mcrpc.exceptions import RpcError


class TestRpcClient(unittest.TestCase):
    """Tests for `mcrpc` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.c = RpcClient(
            '127.0.0.1', '7010', 'testuser', 'testpassword', False
        )

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_getinfo(self):
        """Test something."""
        r = self.c.getinfo()
        self.assertIsInstance(r, dict)

    def test_nonexisting_method(self):
        with self.assertRaises(RpcError):
            self.c.noexist()



