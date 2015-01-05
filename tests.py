# -*- coding: utf-8 -*-

import unittest

from dijkstra import dijkstra
from sqrt import sqrt
from binary_search import binary_search
from lcs import lcs
from lis import lis
from permutation import perm
from well_formed_brackets import brackets
from power_set import power_set
from quicksort import quicksort
from mergesort import mergesort
from same_digits_next_bigger import next_bigger
from phonewords import phonewords
from mix_sets import mix_sets
from palindrome_insertions import palindrome_insertions
from kmp import kmp


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
        self.assertEqual(sqrt(0.4), 0.632)
        self.assertEqual(sqrt(100), 10.0)
        self.assertEqual(sqrt(12), 3.464)

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 3, 4, 6, 8, 9, 11], 4), 2)
        self.assertEqual(binary_search([1, 3, 4, 6, 8, 9, 11], 6), 3)
        self.assertEqual(binary_search([1, 3, 4, 6, 8, 9, 11], 8), 4)
        self.assertEqual(binary_search([1, 3, 4, 6, 8, 9, 11], 1), 0)
        self.assertEqual(binary_search([1, 3, 4, 6, 8, 9, 11], 11), 6)
        self.assertIsNone(binary_search([], 100))
        self.assertIsNone(binary_search([1, 5, 10], 100))
        self.assertIsNone(binary_search([1, 5, 10], -1))

    def test_longest_common_subsequence(self):
        self.assertEqual(lcs("waaaa", "bbbbasfaaewra"), "aaaa")
        self.assertEqual(lcs("abc", "def"), "")
        self.assertEqual(lcs("123", "01234"), "123")
        self.assertEqual(lcs("abcd", "dcba"), "c")

    def test_longest_increasing_subsequence(self):
        self.assertListEqual(
            lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]),
            [0, 2, 6, 9, 11, 15]
        )
        self.assertListEqual(
            lis([1, 10, 100, 1000, 2, 3, 4, 5, 10, 20, 6, 7, 8]),
            [1, 2, 3, 4, 5, 6, 7, 8]
        )

    def test_permutations(self):
        self.assertListEqual(perm([1, 2, 3, 4]),
                             [[1, 2, 4, 3],
                              [1, 3, 2, 4],
                              [1, 3, 4, 2],
                              [1, 4, 2, 3],
                              [1, 4, 3, 2],
                              [2, 1, 3, 4],
                              [2, 1, 4, 3],
                              [2, 3, 1, 4],
                              [2, 3, 4, 1],
                              [2, 4, 1, 3],
                              [2, 4, 3, 1],
                              [3, 1, 2, 4],
                              [3, 1, 4, 2],
                              [3, 2, 1, 4],
                              [3, 2, 4, 1],
                              [3, 4, 1, 2],
                              [3, 4, 2, 1],
                              [4, 1, 2, 3],
                              [4, 1, 3, 2],
                              [4, 2, 1, 3],
                              [4, 2, 3, 1],
                              [4, 3, 1, 2],
                              [4, 3, 2, 1]])
        self.assertListEqual(perm(["A", "B", "C"]),
                             [["A", "C", "B"],
                              ["B", "A", "C"],
                              ["B", "C", "A"],
                              ["C", "A", "B"],
                              ["C", "B", "A"]])

    def test_bracket_combinations(self):
        self.assertListEqual(brackets(1),
                             ["()"])
        self.assertListEqual(brackets(2),
                             ["(())",
                              "()()"])
        self.assertListEqual(brackets(3),
                             ["((()))",
                              "(()())",
                              "(())()",
                              "()(())",
                              "()()()"])

    def test_power_set(self):
        self.assertSetEqual(power_set({"A", "B", "C"}),
                            {frozenset({"A", "B", "C"}),
                             frozenset({"A", "B"}),
                             frozenset({"A", "C"}),
                             frozenset({"B", "C"}),
                             frozenset({"A"}),
                             frozenset({"B"}),
                             frozenset({"C"}),
                             frozenset()})

    def test_quicksort(self):
        self.assertListEqual(quicksort([3, 7, 8, 5, 2, 1, 9, 5, 4]),
                             [1, 2, 3, 4, 5, 5, 7, 8, 9])

    def test_mergesort(self):
        self.assertListEqual(mergesort([6, 5, 3, 1, 8, 7, 2, 4]),
                             [1, 2, 3, 4, 5, 6, 7, 8])

    def test_same_digits_next_bigger(self):
        self.assertEqual(next_bigger(38276),
                         38627)
        self.assertEqual(next_bigger(123456784987654321),
                         123456785123446789)

        self.assertIsNone(next_bigger(1111))
        self.assertIsNone(next_bigger(54321))

    def test_phonewords(self):
        self.assertListEqual(phonewords("10-34"),
                             ["10DG", "10DH", "10DI", "10EG", "10EH", "10EI",
                              "10FG", "10FH", "10FI"])
        self.assertListEqual(phonewords("1202"),
                             ["1A0A", "1A0B", "1A0C", "1B0A", "1B0B", "1B0C",
                              "1C0A", "1C0B", "1C0C"])
        self.assertListEqual(phonewords("000-111"),
                             ["000111"])

    def test_mix_sets(self):
        self.assertListEqual(mix_sets([["A", "B"], ["C"], ["D", "E"]]),
                             ["ACD", "ACE", "BCD", "BCE"])

    def test_palindrome_insertions(self):
        self.assertListEqual(palindrome_insertions("ab"),
                             ["b"])
        self.assertListEqual(palindrome_insertions("aa"),
                             [])
        self.assertListEqual(palindrome_insertions("abcd"),
                             ["d", "c", "b"])
        self.assertListEqual(palindrome_insertions("abcda"),
                             ["d", "c"])
        self.assertListEqual(palindrome_insertions("abcde"),
                             ["e", "d", "c", "b"])

    def test_kmp(self):
        self.assertListEqual(kmp("THIS IS A TEST TEXT", "TEST"),
                             [10])
        self.assertListEqual(kmp("AABAACAADAABAAABAA", "AABA"),
                             [0, 9, 13])
        self.assertListEqual(kmp("AAAAAAAAAAAAAAAAAB", "AAAAB"),
                             [13])
        self.assertListEqual(kmp("ABABABCABABABCABABABC", "ABABAC"),
                             [])
        self.assertListEqual(kmp("ABC ABCDAB ABCDABCDABDE", "ABCDABD"),
                             [15])


if __name__ == "__main__":
    unittest.main()
