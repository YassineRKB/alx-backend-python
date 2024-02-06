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


class TestGetJson(unittest.TestCase):
    """unitest for get_json func"""
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    def test_get_json(self, url, payload):
        """test case for get_json func"""
        mock_response = Mock()
        mock_response.json.return_value = payload
        with patch('requests.get', return_value=mock_response) as mockingbird_get:
            cpx = get_json(url)
        mockingbird_get.assert_called_once_with(url)
        self.assertEqual(cpx, payload)


class TestMemoize(unittest.TestCase):
    """unitest for memoize func"""
    def test_memoize(self):
        """test case for memoize func"""
        class TestClass:
            """test class"""
            def a_method(self):
                """a method"""
                return 42

            @memoize
            def a_property(self):
                """a property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mockingbird:
            mockingbird.return_value = 42
            tc = TestClass()
            res1 = tc.a_property
            res2 = tc.a_property
            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)
            mockingbird.assert_called_once()
