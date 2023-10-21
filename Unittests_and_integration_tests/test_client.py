#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ('google', 'Google'),
        ('abc', 'ABC')
    ])
    @patch('client.GithubOrgClient.get_json', return_value={"name": "Google"})
    def test_org(self, org_name, expected_name, mock_get_json):
        client = GithubOrgClient(org_name)
        org_info = client.org()

        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')
        self.assertEqual(org_info, {"name": expected_name})

    def test_public_repos_url(self):
        org_payload = {
            "repos_url": "https://api.github.com/orgs/exampleorg/repos"
        }

        with patch('client.GithubOrgClient.org', return_value=org_payload):
            client = GithubOrgClient("exampleorg")

            public_repos_url = client._public_repos_url

            self.assertEqual(public_repos_url,
                             "https://api.github.com/orgs/exampleorg/repos")


if __name__ == '__main__':
    unittest.main()
