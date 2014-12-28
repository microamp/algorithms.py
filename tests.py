# -*- coding: utf-8 -*-

import unittest

from dijkstra import dijkstra
from sq_root import square_root
from binary_search import binary_search
from longest_common_subsequence import lcs
from longest_increasing_subsequence import lis


class TestAlgorithms(unittest.TestCase):
    def test_dijkstra(self):
        graph = {
            "a": {"b": 7, "c": 9, "f": 14},
            "b": {"a": 7, "c": 10, "d": 15},
            "c": {"a": 9, "b": 10, "d": 11, "f": 2},
            "d": {"b": 15, "c": 11, "e": 6},
            "e": {"d": 6, "f": 9},
            "f": {"a": 14, "c": 2, "e": 9},
        }
        x, y = "a", "e"  # shortest distance from 'a' to 'e'

        distance, path = dijkstra(graph, x, y)
        self.assertEqual(distance, 20)
        self.assertListEqual(path, ["a", "c", "f", "e"])

    def test_sq_root(self):
        self.assertEqual(square_root(0.4), 0.632)
        self.assertEqual(square_root(100), 10.0)
        self.assertEqual(square_root(12), 3.464)

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 3, 4, 6, 8, 9, 11], 4), 2)
        self.assertEqual(binary_search([1, 3, 4, 6, 8, 9, 11], 6), 3)
        self.assertEqual(binary_search([1, 3, 4, 6, 8, 9, 11], 8), 4)
        self.assertEqual(binary_search([1, 3, 4, 6, 8, 9, 11], 1), 0)
        self.assertEqual(binary_search([1, 3, 4, 6, 8, 9, 11], 11), 6)
        self.assertIsNone(binary_search([], 100))
        self.assertIsNone(binary_search([1, 5, 10], 100))
        self.assertIsNone(binary_search([1, 5, 10], -1))

    def test_longest_common_sequence(self):
        self.assertEqual(lcs("waaaa", "bbbbasfaaewra"), "aaaa")
        self.assertEqual(lcs("abc", "def"), "")
        self.assertEqual(lcs("123", "01234"), "123")
        self.assertEqual(lcs("abcd", "dcba"), "c")

    def test_longest_increasing_sequence(self):
        self.assertListEqual(
            lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]),
            [0, 2, 6, 9, 11, 15]
        )
        self.assertListEqual(
            lis([1, 10, 100, 1000, 2, 3, 4, 5, 10, 20, 6, 7, 8]),
            [1, 2, 3, 4, 5, 6, 7, 8]
        )


if __name__ == "__main__":
    unittest.main()
