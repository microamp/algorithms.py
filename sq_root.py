# -*- coding: utf-8 -*-

"""
Find the square root of a number

Links:
* Newton's method:
https://en.wikipedia.org/wiki/Newton%27s_method
"""

ACCURACY = 3
first_guess = lambda n: n / 2


def sqrt(n, f=None, f_deriv=None, guess=None):
    # print("guess: {0}".format(guess))
    new_guess = guess - (f(guess) / f_deriv(guess))
    return (round(new_guess, ACCURACY)
            if round(guess, ACCURACY) == round(new_guess, ACCURACY) else
            sqrt(n, f=f, f_deriv=f_deriv, guess=new_guess))


def square_root(n):
    return sqrt(n,
                f=lambda x: pow(x, 2) - n,
                f_deriv=lambda x: 2 * x,
                guess=first_guess(n))
