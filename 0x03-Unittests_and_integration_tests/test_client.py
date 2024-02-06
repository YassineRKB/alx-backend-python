#!/usr/bin/env python3
"""module for testing client.py"""
import unittest
from unittest import mock
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib import request


class TestGithubOrgClient(unittest.TestCase):
    """unitest for GithubOrgClient class"""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org, mock):
        """test case for GithubOrgClient.org"""
        goc = GithubOrgClient(org)
        goc.org()
        link = f'https://api.github.com/orgs/{org}'
        mock.assert_called_once_with(link)
