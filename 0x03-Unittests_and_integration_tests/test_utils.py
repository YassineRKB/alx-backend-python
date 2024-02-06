#!/usr/bin/env python3
"""module for testing utils.py"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import memoize, access_nested_map, get_json

class TestAccessNestedMap(unittest.TestCase):
    """unitest for access_nested_map func"""
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, map, path, expected):
        """test case for access_nested_map func"""
        self.assertEqual(access_nested_map(map, path), expected)
