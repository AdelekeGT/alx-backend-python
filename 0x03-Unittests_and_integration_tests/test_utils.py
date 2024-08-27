#!/usr/bin/env python3
"""Parametize a unit test"""

import unittest
from parameterized import parameterized


def access_nested_map(nested_map, path):
    """Retrieve the value from a nested map following the given path"""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Unit test for utils.access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test the access_nested_map function with parameterized inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
