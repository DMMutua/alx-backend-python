#!/usr/bin/env python3
"""Unit Test Script"""

import unittest
from unittest import mock
from parameterized import parameterized
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json
memoize = __import__("utils").memoize


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

    @parameterized.expand([
        ({}, ("a",), KeyError("a")),
        ({"a": 1}, ("a", "b"), KeyError("b")),
        ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception):
        """using `assertRaises` as context manager to test
        error as part of Unit Test"""

        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(expected_exception))


class TestGetJson(unittest.TestCase):
    """A Class with methods that do unit tests to
    functions that retrieve JSON Objects"""

    @mock.patch('utils.requests.get')
    def test_get_json(self, mock_get):
        """A Method to test the utils.get_json Method"""

        test_cases = [
                ("http://example.com", {"payload": True}),
                ("http://holberton.io", {"payload": False})
                ]

        for test_url, test_payload in test_cases:
            mock_get.reset_mock()  # Reseting mock object before each iteration

            mock_response = mock.Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """A Class with Methods that tests memoized Functions"""

    def test_memoize(self):
        """Tests Memoization Function"""

        class TestClass:
            """A Testing Class"""

            def a_method(self):
                """a sample method"""
                return 42

            @memoize
            def a_property(self):
                """A sample property"""
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42
            test_instance = TestClass()
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_a_method.assert_called_once()


# Running tests
if __name__ == '__main__':
    unittest.main()
