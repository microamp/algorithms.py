# -*- coding: utf-8 -*-

"""
Merge sort

* Links:
Merge sort:
https://en.wikipedia.org/wiki/Merge_sort
"""

from operator import add


def sort_(list1, list2, sorted_=None):
    if not list1 and not list2:
        return sorted_
    elif not list1:
        return sort_(list1, list2[1:], add(sorted_, list2[:1]))
    elif not list2:
        return sort_(list1[1:], list2, add(sorted_, list1[:1]))
    else:
        return (sort_(list1[1:], list2, add(sorted_, list1[:1]))
                if list1[0] < list2[0] else
                sort_(list1, list2[1:], add(sorted_, list2[:1])))


def _mergesort(lists):
    if len(lists) == 1:
        return lists[0]
    else:
        return _mergesort([sort_(lists[i], lists[i + 1], sorted_=[])
                           for i in range(0, len(lists), 2)])


def mergesort(list_):
    return _mergesort([[item] for item in list_]) if list_ else []
