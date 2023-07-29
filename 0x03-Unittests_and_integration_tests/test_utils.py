#!/usr/bin/env python3
"""
unit test for utils.access_nested_map
"""

import unittest
from typing import Dict, Tuple, Union
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
    def test_access_nested_map(
        self,
        nested_map: Dict,
        path: Tuple,
        expected: Union[Dict, int]
    ) -> None:
        """
        TestAccessNestedMap method
        """
        nested_map = {"a": {"b": {"c": 1}}}
        self.assertEqual(access_nested_map(nested_map, ["a", "b", "c"]), 1)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Dict,
        path: Tuple,
        expected: Union[Dict, int]
    ) -> None:
        """
        TestAccessNestedMap method
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
