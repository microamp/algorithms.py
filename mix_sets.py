# -*- coding: utf-8 -*-

"""
Mix and combine sets of cells to list all possible combinations
"""

from operator import add


def _mix_sets(sets, joined=None):
    if not sets:
        return joined
    else:
        return _mix_sets(sets[1:], joined=[add(x, [y])
                                           for x in joined for y in sets[0]])


def mix_sets(sets):
    return list(map(lambda set_: "".join(set_),
                    _mix_sets(sets, joined=[[]])))
