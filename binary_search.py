# -*- coding: utf-8 -*-

"""
Binary search algorithm

Links:
* Binary search algorithm:
https://en.wikipedia.org/wiki/Binary_search_algorithm
"""


def find_idx_mid(idx_min, idx_max):
    return idx_min + int((idx_max - idx_min) / 2)


def _bin_search(list_, x, idx_min=0, idx_max=0):
    if idx_min > idx_max:
        return None
    else:
        idx_mid = find_idx_mid(idx_min, idx_max)
        if x == list_[idx_mid]:
            return idx_mid
        elif x < list_[idx_mid]:
            return _bin_search(list_, x, idx_min=idx_min, idx_max=idx_mid - 1)
        else:
            return _bin_search(list_, x, idx_min=idx_mid + 1, idx_max=idx_max)


def binary_search(list_, x):
    return (None if not list_ else
            _bin_search(list_, x, idx_min=0, idx_max=len(list_) - 1))
