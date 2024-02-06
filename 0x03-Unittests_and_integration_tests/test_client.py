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

    @parameterized.expand([
        ('random_url', {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result):
        """test case for GithubOrgClient._public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            res = GithubOrgClient(name)._public_repos_url
            self.assertEqual(res, result.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mock):
        """test case for GithubOrgClient.public_repos"""
        payload = [{"name": "google"}, {"name": "abc"}]
        mock.return_value = payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:
            mock_public.return_value = "http://some_url.com"
            res = GithubOrgClient('test').public_repos()
            self.assertEqual(
                res,
                ['google', 'abc']
            )
            mock.assert_called_once_with("http://some_url.com")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, expected):
        """test case for GithubOrgClient.has_license"""
        res = GithubOrgClient.has_license(repo, license)
        self.assertEqual(res, expected)


@parameterized_class(['org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'], TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """unitest for GithubOrgClient class with integration tests"""
    @classmethod
    def setUpClass(cls):
        """init class"""
        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """end class"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test case for GithubOrgClient.public_repos"""
        tc = GithubOrgClient("google")
        self.assertEqual(tc.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """test case for GithubOrgClient.public_repos with license"""
        with patch('client.GithubOrgClient.has_license',
                   return_value=True) as licensedMockingBird:
            tc = GithubOrgClient("google")
            self.assertEqual(
                tc.public_repos("apache-2.0"), self.apache2_repos
            )
