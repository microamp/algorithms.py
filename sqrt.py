# -*- coding: utf-8 -*-

"""
Newton's method (for finding successively better approximation to the roots of
a real-valued function)

Links:
* Newton's method:
https://en.wikipedia.org/wiki/Newton%27s_method
"""

ACCURACY = 3
first_guess = lambda n: n / 2


def _sqrt(n, f=None, f_deriv=None, guess=None):
    new_guess = guess - (f(guess) / f_deriv(guess))
    rounded = round(new_guess, ACCURACY)
    if rounded == round(guess, ACCURACY):
        return rounded
    else:
        return _sqrt(n, f=f, f_deriv=f_deriv, guess=new_guess)


def sqrt(n):
    return _sqrt(n,
                 f=lambda x: pow(x, 2) - n,
                 f_deriv=lambda x: 2 * x,
                 guess=first_guess(n))
