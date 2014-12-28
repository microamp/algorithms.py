# -*- coding: utf-8 -*-

"""
Longest increasing subsequence

Links:
* Longest Monotonically Increasing Subsequence Size (N log N):
http://ow.ly/GuPXM
* Longest increasing subsequence:
http://en.wikipedia.org/wiki/Longest_increasing_subsequence
"""

from copy import copy
from itertools import filterfalse


def lt_all(subseqs, item):
    return all(item < s[-1] for s in subseqs)


def gt_all(subseqs, item):
    return all(item > s[-1] for s in subseqs)


def largest_seq(subseqs):
    return max(subseqs, key=len)


def largest_end_seq(subseqs, item):
    return max(filter(lambda s: s[-1] < item, subseqs),
               key=lambda s: s[-1])


def filter_seqs(subseqs, length):
    return list(filterfalse(lambda s: len(s) == length, subseqs))


def lis(seq):
    """
    1. If A[i] is smallest among all end candidates of active lists, we will
    start new active list of length 1.
    2. If A[i] is largest among all end candidates of active lists, we will
    clone the largest active list, and extend it by A[i].
    3. If A[i] is in between, we will find a list with largest end element that
    is smaller than A[i]. Clone and extend this list by A[i]. We will discard
    all other lists of same length as that of this modified list.
    (link: http://ow.ly/GuPXM)
    """
    subseqs = []
    for item in seq:
        if lt_all(subseqs, item):
            subseqs.append([item])
        elif gt_all(subseqs, item):
            _seq = copy(largest_seq(subseqs))
            _seq.append(item)
            subseqs.append(_seq)
        else:
            _seq = copy(largest_end_seq(subseqs, item))
            _seq.append(item)
            subseqs = filter_seqs(subseqs, len(_seq))
            subseqs.append(_seq)
    return max(subseqs, key=len)
