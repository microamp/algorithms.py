# -*- coding: utf-8 -*-

"""
Conway's Game of Life

* Links:
Conway's Game of Life:
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
"""


from collections import Counter
from operator import add


def range_(p, size):
    lower, upper = p - 1, p + 2
    return range(lower if lower >= 0 else 0,
                 upper if upper <= size else size)


def neighbour_count(live_cells, size, neighbours=None):
    if not live_cells:
        return Counter(neighbours)
    x, y = live_cells[0]
    return neighbour_count(live_cells[1:], size,
                           neighbours=add(neighbours or [],
                                          [(xx, yy) for xx in range_(x, size)
                                           for yy in range_(y, size)
                                           if (xx, yy) != (x, y)]))


def is_live(live_cells, xy, count):
    return ((xy in live_cells and count in (2, 3)) or
            (xy not in live_cells and count == 3))


def tick(live_cells=(), size=3):
    # keep track of live cells in `size` x `size` matrix
    # everything else = dead cell
    while True:
        live_cells = tuple(xy
                           for xy, count
                           in neighbour_count(live_cells, size).items()
                           if is_live(live_cells, xy, count))
        yield live_cells  # generator for potentially infinite patterns
