#!/usr/bin/env python3
"""
unit test for utils.access_nested_map
"""

import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self):
        """
        TestAccessNestedMap method
        """
        nested_map = {"a": {"b": {"c": 1}}}
        self.assertEqual(access_nested_map(nested_map, ["a", "b", "c"]), 1)
