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

    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError),
    ])
    def test_access_nested_map_exception(self, map, path, expected):
        """test case for access_nested_map func"""
        with self.assertRaises(expected):
            access_nested_map(map, path)
