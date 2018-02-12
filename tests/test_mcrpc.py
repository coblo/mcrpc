#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `mcrpc` package."""
import unittest
from string import Template

from codegen import get_api_methods, get_stub_template
from mcrpc import RpcClient
from mcrpc.exceptions import RpcError


class TestMCRPC(unittest.TestCase):
    """Tests for `mcrpc` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.c = RpcClient(
            '127.0.0.1', '7010', 'testuser', 'testpassword', False
        )

    def test_getinfo(self):
        """Test something."""
        r = self.c.getinfo()
        self.assertIsInstance(r, dict)

    def test_nonexisting_method(self):
        with self.assertRaises(RpcError):
            self.c.noexist()

    def test_load_stub_template(self):
        self.assertIsInstance(get_stub_template(), Template)

    def test_get_api_methods(self):
        methods = get_api_methods(self.c)
        self.assertEqual(len(methods), 148)
        self.c.getinfo()
