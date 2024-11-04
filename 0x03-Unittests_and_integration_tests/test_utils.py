"""
Python module that uses
unittests to test the utils module
"""
#!/usr/bin/env python3
from unittest import TestCase, main
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """ Class to test a nested map
    """
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Method to test a nested map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

if __name__ == "__main__":
    main()
