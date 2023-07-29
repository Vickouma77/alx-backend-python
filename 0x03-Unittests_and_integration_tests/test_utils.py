#!/usr/bin/env python3
"""
unit test for utils.access_nested_map
"""

import unittest

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class
    """

    def test_access_nested_map(self):
        """
        TestAccessNestedMap method
        """
        nested_map = {"a": {"b": {"c": 1}}}
        self.assertEqual(access_nested_map(nested_map, ["a", "b", "c"]), 1)
