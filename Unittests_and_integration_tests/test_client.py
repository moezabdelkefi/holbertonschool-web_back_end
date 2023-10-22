#!/usr/bin/env python3
"""test-client-server"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test Github Organization"""
    @parameterized.expand([
        ('google', 'Google'),
        ('abc', 'ABC')
    ])
    @patch('client.GithubOrgClient.get_json', return_value={"name": "Google"})
    def test_org(self, org_name, expected_name, mock_get_json):
        """Test organization retrieval with json"""
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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        client = GithubOrgClient("exampleorg")

        result = client.has_license(repo, license_key)

        self.assertEqual(result, expected_result)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get')

        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url == "https://api.github.com/orgs/exampleorg":
                return cls.org_payload
            elif url == "https://api.github.com/orgs/exampleorg/repos":
                return cls.repos_payload
            elif url == "https://api.github.com/orgs/exampleorg/repos?license=apache-2.0":
                return cls.apache2_repos
            else:
                return None

        cls.mock_get.return_value.json.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        client = GithubOrgClient("exampleorg")

        repos = client.public_repos()

        self.assertEqual(repos, self.expected_repos)


if __name__ == '__main__':
    unittest.main()
