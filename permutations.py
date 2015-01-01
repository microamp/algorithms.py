# -*- coding: utf-8 -*-

"""
Find all permutations of array

Links:
* Permutation:
https://en.wikipedia.org/wiki/Permutation
"""

from copy import copy
from operator import add


def find_k(seq):
    try:
        return max(filter(lambda k: seq[k] < seq[k + 1],
                          range(len(seq) - 1)))
    except ValueError:
        return None


def find_l(seq, k):
    try:
        return max(filter(lambda l: seq[k] < seq[l],
                          range(k + 1, len(seq))))
    except ValueError:
        return None


def swap(seq, k, l):
    temp = copy(seq)
    temp[k], temp[l] = seq[l], seq[k]
    return temp


def reverse(seq, k):
    return add(seq[:k + 1], seq[k + 1:][::-1])


def _perm(seq, seqs=None):
    k = find_k(seq)
    if k is None:
        return seqs
    else:
        l = find_l(seq, k)
        new_seq = reverse(swap(seq, k, l), k)
        return _perm(new_seq, add(seqs, [new_seq]))


def perm(seq):
    """
    1. Find the largest index k such that a[k] < a[k + 1]. If no such index
    exists, the permutation is the last permutation.
    2. Find the largest index l greater than k such that a[k] < a[l].
    3. Swap the value of a[k] with that of a[l].
    4. Reverse the sequence from a[k + 1] up to and including the final element
    a[n].
    """
    return _perm(seq, seqs=[])
