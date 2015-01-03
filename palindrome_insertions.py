# -*- coding: utf-8 -*-

"""
Find the minimum insertions needed to make a word palindrome

* Links:
Minimum insertions to form a palindrome:
http://ow.ly/GJpfJ
"""

from operator import add


def _palindrome_insertions(s, insertions=None):
    if len(s) in (0, 1,):
        return insertions
    else:
        new_s, new_insertions = ((s[1:-1], insertions) if s[0] == s[-1] else
                                 (add(s[-1], s), add(insertions, [s[-1]])))
        return _palindrome_insertions(new_s, insertions=new_insertions)


def palindrome_insertions(s):
    return _palindrome_insertions(s, insertions=[])
