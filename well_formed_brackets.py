# -*- coding: utf-8 -*-

"""
Finding all combinations of well-formed brackets

* Links:
Finding all combinations of well-formed brackets:
http://ow.ly/GEl9l
"""


def next_patterns(n, pattern):
    opened, closed = pattern.count("("), pattern.count(")")
    return filter(None, [pattern + "(" if opened < n else None,
                         pattern + ")" if closed < opened else None])


def _brackets(n, patterns):
    if any(len(p) == n * 2 for p in patterns):
        return patterns
    return _brackets(n, [p2 for p1 in patterns
                         for p2 in next_patterns(n, p1)])


def brackets(n):
    return _brackets(n, [""])
