#!/usr/bin/env python3
"""Unit Test Script"""

import unittest
from parameterized import parameterized
access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """A Class to test the `access_nested_map` class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Testing access_nested_map Method"""

        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)


# Running tests
if __name__ == '__main__':
    unittest.main()
