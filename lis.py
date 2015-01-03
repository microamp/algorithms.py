# -*- coding: utf-8 -*-

"""
Longest increasing subsequence

Links:
* Longest Monotonically Increasing Subsequence Size (N log N):
http://ow.ly/GuPXM
* Longest increasing subsequence:
http://en.wikipedia.org/wiki/Longest_increasing_subsequence
"""

from itertools import filterfalse
from operator import add


def lt_all(subseqs, item):
    return all(item < s[-1] for s in subseqs)


def gt_all(subseqs, item):
    return all(item > s[-1] for s in subseqs)


def largest_seq(subseqs):
    try:
        return max(subseqs, key=len)
    except ValueError:
        return None


def largest_end_seq(subseqs, item):
    try:
        return max(filter(lambda s: s[-1] < item, subseqs),
                   key=lambda s: s[-1])
    except ValueError:
        return None


def filter_seqs(subseqs, length):
    return list(filterfalse(lambda s: len(s) == length, subseqs))


def _lis(seq, subseqs=None):
    if not seq:
        return max(subseqs, key=len)
    else:
        head, tail = seq[0], seq[1:]
        if lt_all(subseqs, head):
            return _lis(tail, add(subseqs, [[head]]))
        elif gt_all(subseqs, head):
            expanded = largest_seq(subseqs) + [head]
            return _lis(tail, add(subseqs, [expanded]))
        else:
            expanded = largest_end_seq(subseqs, head) + [head]
            return _lis(tail, add(filter_seqs(subseqs, len(expanded)),
                                  [expanded]))


def lis(seq):
    """
    1. If A[i] is smallest among all end candidates of active lists, we will
    start new active list of length 1.
    2. If A[i] is largest among all end candidates of active lists, we will
    clone the largest active list, and extend it by A[i].
    3. If A[i] is in between, we will find a list with largest end element that
    is smaller than A[i]. Clone and extend this list by A[i]. We will discard
    all other lists of same length as that of this modified list.
    (http://ow.ly/GuPXM)
    """
    return _lis(seq, subseqs=[])
