# -*- coding: utf-8 -*-

"""
Power set

* Links:
Power set:
http://en.wikipedia.org/wiki/Power_set
How can I create a Set of Sets in Python?:
http://ow.ly/GFWoh
"""


def add_item(sets, item):
    return {s.union({item}) for s in sets}


def power_set(s):
    """
    In other words, the power set of the empty set is the set containing the
    empty set and the power set of any other set is all the subsets of the set
    containing some specific element and all the subsets of the set not
    containing that specific element.
    (http://en.wikipedia.org/wiki/Power_set)
    """
    if not len(s):  # base case
        return {frozenset()}
    else:  # inductive case
        item = next(iter(s))  # first item
        without_item = power_set(s.difference({item}))
        return without_item.union(add_item(without_item, item))
