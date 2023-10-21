#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json


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
    @unittest.mock.patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = test_payload
        mock_requests_get.return_value = mock_response

        result = get_json(test_url)
        mock_requests_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
