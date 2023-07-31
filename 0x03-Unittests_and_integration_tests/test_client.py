#!/usr/bin/env python3
"""
Unittests for client.py
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient
from typing import (
    Dict,
    Tuple,
    Union
)


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class
    """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """
        TestOrg method
        """
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name))

    def test_public_repos_url(self) -> None:
        """
        TestPublicReposUrl method
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "test"}
            test_class = GithubOrgClient("test")
            self.assertEqual(test_class._public_repos_url, "test")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """
        TestPublicRepos method
        """
        mock_get_json.return_value = [{"name": "Google"}, {"name": "abc"}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "test"
            test_class = GithubOrgClient("test")
            self.assertEqual(test_class.public_repos(), ["Google", "abc"])
            mock_get_json.assert_called_once_with("test")

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, "my_license", True),
        ({'license': {'key': 'other_license'}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict[str, Dict], license_key: str,
                            expected_return: bool) -> None:
            """
            TestHasLicense method
            """
            test_class = GithubOrgClient("test")
            self.assertEqual(test_class.has_license(repo, license_key),
                            expected_return)
