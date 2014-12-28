# -*- coding: utf-8 -*-

"""
Longest common subsequence problem

Links:
* Longest common subsequence problem:
https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
"""


def lcs(x, y):
    # print("x: {x}, y: {y}".format(x=x, y=y))
    if not x or not y:
        return ""
    else:
        if x[-1] == y[-1]:
            return lcs(x[:-1], y[:-1]) + x[-1]
        else:
            return (lcs(x[:-1], y) if len(x) > len(y) else
                    lcs(x, y[:-1]))
