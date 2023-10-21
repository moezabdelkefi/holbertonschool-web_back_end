#!/usr/bin/env python3
"""test-client-server"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
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

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """ Test more public repos """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:
            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()


if __name__ == '__main__':
    unittest.main()
