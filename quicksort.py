# -*- coding: utf-8 -*-

"""
Quicksort

* Links:
Quicksort:
http://en.wikipedia.org/wiki/Quicksort
"""

from functools import reduce
from operator import add
from itertools import filterfalse


def join(*lists):
    return reduce(lambda l1, l2: add(l1, l2), lists)


def lt_pivot(seq, pivot):
    return list(filter(lambda v: v < pivot, seq))


def gte_pivot(seq, pivot):
    return list(filterfalse(lambda v: v < pivot, seq))


def quicksort(seq):
    if len(seq) in (0, 1,):  # base case (no sorting required)
        return seq
    else:  # inductive case
        pivot = seq[-1]  # always select last item as pivot
        return join(quicksort(lt_pivot(seq[:-1], pivot)),
                    [pivot],
                    quicksort(gte_pivot(seq[:-1], pivot)))
