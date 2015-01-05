# -*- coding: utf-8 -*-

"""
Knuth–Morris–Pratt algorithm

* Links:
Knuth–Morris–Pratt algorithm:
http://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
"""


from operator import add


def partial_match_table(w):  # TODO: optimisation
    def biggest_len_common(w):
        def proper_prefixes():
            return {w[:i] for i in range(1, len(w))}

        def proper_suffixes():
            return {w[i:] for i in range(len(w) - 1, 0, -1)}

        try:
            return max(map(len,
                           proper_prefixes().intersection(proper_suffixes())))
        except ValueError:
            return 0

    return [biggest_len_common(w[:i + 1]) for i in range(len(w))]


def _kmp(s, w, t, m=0, i=0, indices=None):
    if i == len(w):  # fully matched
        i, indices = 0, add(indices, [m - len(w)])

    if m == len(s):
        return indices
    else:
        if s[m] == w[i]:  # matched
            m, i = m + 1, i + 1
        else:  # mismatched, look for partial matches
            partial_matches = t[i - 1]
            if partial_matches:
                m, i = m, partial_matches
            else:
                m, i = m + 1, 0

        return _kmp(s, w, t, m=m, i=i, indices=indices)


def kmp(s, w):
    return _kmp(s, w, partial_match_table(w), indices=[])
