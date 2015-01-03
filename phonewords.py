# -*- coding: utf-8 -*-

"""
Phone number to words

Links:
* Phone number to words:
http://www.mobilefish.com/services/phonenumber_words/phonenumber_words.php
"""

from operator import add

DIGIT_TO_WORDS = {
    "2": ("A", "B", "C",),
    "3": ("D", "E", "F",),
    "4": ("G", "H", "I",),
    "5": ("J", "K", "L",),
    "6": ("M", "N", "O",),
    "7": ("P", "Q", "R", "S",),
    "8": ("T", "U", "V",),
    "9": ("W", "X", "Y", "Z",),
}

IGNORE = ("-", "(", ")",)


def _phonewords(numbers):
    if not numbers:
        return [[]]
    else:
        return [add([n], x)
                for n in DIGIT_TO_WORDS.get(numbers[0], [numbers[0]])
                for x in _phonewords(numbers[1:])]


def phonewords(code):
    return list(map(lambda seq: "".join(seq),
                    _phonewords(list(filter(lambda x: x not in IGNORE,
                                            code)))))
