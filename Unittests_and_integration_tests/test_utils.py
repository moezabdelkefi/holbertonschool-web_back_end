#!/usr/bin/env python3
"""testing module for testing functions"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json, memoize
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


class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_requests_get.return_value = mock_response

        result = get_json(test_url)
        mock_requests_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    class TestClass:
        """class TestMemoize with Memoize class"""

        def a_method(self):
            """return a Memoize method"""
            return 42

        @memoize
        def a_property(self):
            """return a Memoize property"""
            return self.a_method()

    def test_memoize(self):
        """test Memoize with Memoize class"""
        test_instance = self.TestClass()

        with patch.object(test_instance, 'a_method') as mock_a_method:
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()

            mock_a_method.assert_called_once()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == "__main__":
    unittest.main()
