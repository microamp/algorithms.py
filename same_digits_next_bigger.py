# -*- coding: utf-8 -*-

"""
Find the next higher number with the same set of digits

* Links:
Given a number, find the next higher number which has the exact same set of
digits as the original number:
http://ow.ly/GGzpE
"""

from functools import reduce
from operator import add


def join(*lists):
    return reduce(lambda list1, list2: add(list1, list2), lists)


def smallest_bigger(digit, digits):
    try:
        return min(filter(lambda d: d > digit, digits))
    except ValueError:
        return None


def _next_bigger(digits1, digits2):
    if not digits1:
        return None
    else:
        bigger = smallest_bigger(digits2[0], digits2[1:])
        if bigger:
            index = digits2.index(bigger)
            # swap items around, mutation :(
            digits2[0], digits2[index] = digits2[index], digits2[0]
            return join(digits1, [digits2[0]], sorted(digits2[1:]))
        else:
            return _next_bigger(digits1[:-1],
                                join(digits1[-1:], digits2))


def next_bigger(digits):
    def map_to_int(digits):
        return [int(d) for d in digits]

    def ints_to_int(digits):
        return int("".join(map(str, digits)))

    digits_str = [s for s in str(digits)]
    result = _next_bigger(map_to_int(digits_str[:-1]),
                          map_to_int(digits_str[-1:]))
    return ints_to_int(result) if result else None
