# -*- coding: utf-8 -*-

"""
Counting sort

Links:
* Counting sort:
http://en.wikipedia.org/wiki/Counting_sort
"""

from operator import add


def histogram(input, count):
    if not input:
        return count
    count[input[0]] += 1
    return histogram(input[1:], count)


def prefix_sum(hist, prev=0, summed=None):
    if not hist:
        return summed
    next_sum = add(prev, hist[0])
    return prefix_sum(hist[1:], prev=next_sum, summed=add(summed, [next_sum]))


def sort(input, summed, output=None):
    if not input:
        return output
    output[summed[input[0]] - 1] = input[0]  # allocate item
    summed[input[0]] -= 1  # next occurrence to previous position
    return sort(input[1:], summed, output=output)


def counting_sort(input, limit=10):
    return sort(input,
                prefix_sum(histogram(input, [0 for i in range(limit)]),
                           summed=[]),
                output=[-1 for i in range(len(input))])
