#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a' not found in the nested_map"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b' not found in the nested_map")
    ])
    def test_access_nested_map_exception(self, nested_map, path, result):
        """test exception"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
            self.assertEqual(result, e.exception)

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload):
        """Mock HTTP calls"""
        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url=test_url), test_payload)


if __name__ == "__main__":
    unittest.main()
