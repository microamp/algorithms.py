algorithms.py
=============

A port of @sagivo's [algorithms](https://github.com/sagivo/algorithms) in Python 3

Problems
--------

| Problem                                                                                                                                                                                   | Solution                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------                                                                                     |
| [Dijkstra's algorithm for finding the shortest path](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)                                                                                | [dijkstra.py](https://github.com/microamp/algorithms.py/blob/master/dijkstra.py)                               |
| [Newton's method for finding the square root of a number](https://en.wikipedia.org/wiki/Newton%27s_method)                                                                                | [sqrt.py](https://github.com/microamp/algorithms.py/blob/master/sqrt.py)                                       |
| [Binary search algorithm](https://en.wikipedia.org/wiki/Binary_search_algorithm)                                                                                                          | [binary_search.py](https://github.com/microamp/algorithms.py/blob/master/binary_search.py)                     |
| [Longest increasing subsequence](http://en.wikipedia.org/wiki/Longest_increasing_subsequence)                                                                                             | [lis.py](https://github.com/microamp/algorithms.py/blob/master/lis.py)                                         |
| [Longest common subsequence](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)                                                                                            | [lcs.py](https://github.com/microamp/algorithms.py/blob/master/lcs.py)                                         |
| [Quicksort](http://en.wikipedia.org/wiki/Quicksort)                                                                                                                                       | [quicksort.py](https://github.com/microamp/algorithms.py/blob/master/quicksort.py)                             |
| [Mergesort](https://en.wikipedia.org/wiki/Merge_sort)                                                                                                                                     | [mergesort.py](https://github.com/microamp/algorithms.py/blob/master/mergesort.py)                             |
| [Counting sort](http://en.wikipedia.org/wiki/Counting_sort)                                                                                                                               | [counting_sort.py](https://github.com/microamp/algorithms.py/blob/master/counting_sort.py)                     |
| [Shellsort](http://en.wikipedia.org/wiki/Shellsort)                                                                                                                                       | TODO                                                                                                           |
| Mix and combine sets of cells to list all possible combinations                                                                                                                           | [mix_sets.py](https://github.com/microamp/algorithms.py/blob/master/mix_sets.py)                               |
| [Finding all combinations of well-formed brackets](http://stackoverflow.com/questions/727707/finding-all-combinations-of-well-formed-brackets)                                            | [well_formed_brackets.py](https://github.com/microamp/algorithms.py/blob/master/well_formed_brackets.py)       |
| [Phonewords](http://www.mobilefish.com/services/phonenumber_words/phonenumber_words.php)                                                                                                  | [phonewords.py](https://github.com/microamp/algorithms.py/blob/master/phonewords.py)                           |
| [Permutation](https://en.wikipedia.org/wiki/Permutation)                                                                                                                                  | [permutation.py](https://github.com/microamp/algorithms.py/blob/master/permutation.py)                         |
| [Finding the power set of a given set](http://en.wikipedia.org/wiki/Power_set)                                                                                                            | [power_set.py](https://github.com/microamp/algorithms.py/blob/master/power_set.py)                             |
| [Find the next higher number that has the same set of digits](http://stackoverflow.com/questions/9368205/given-a-number-find-the-next-higher-number-which-has-the-exact-same-set-of-digi) | [same_digits_next_bigger.py](https://github.com/microamp/algorithms.py/blob/master/same_digits_next_bigger.py) |
| [Find the minimum insertions needed to form a Palindrome](from http://www.geeksforgeeks.org/dynamic-programming-set-28-minimum-insertions-to-form-a-palindrome/)                          | [palindrome_insertions.py](https://github.com/microamp/algorithms.py/blob/master/palindrome_insertions.py)     |
| [Knuth–Morris–Pratt algorithm](http://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm)                                                                                 | [kmp.py](https://github.com/microamp/algorithms.py/blob/master/kmp.py)                                         |
| [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)                                                                                                            | [game_of_life.py](https://github.com/microamp/algorithms.py/blob/master/game_of_life.py)                       |
| [Knapsack problem](http://en.wikipedia.org/wiki/Knapsack_problem)                                                                                                                         | TODO                                                                                                           |

Goals
-----

- Recursion over imperative looping constructs such as `for`/`while`-loops (1)
- Expressions over stateful methods and mutations (whenever possible)

Neither is easy to achive in OO, however, I believe mutability should be [opt-in](http://bob.ippoli.to/python-haskell-ep2014/#/mutability), not the other way around.

Notes:

1. Recursion is not generally considered a good practice in Python. Python is _not_ a functional programming language, and there is no TCO support in CPython after all. The focus here is, in fact, more on the algorithms despite being implemented in Python.

How to run tests
----------------

All tests can be found in [tests.py](https://github.com/microamp/algorithms.py/blob/master/tests.py). Run the following command to test them.

```bash
python -m tests
```

Versions tested
---------------

- Python 3.2
- Python 3.3
- Python 3.4

TODO
----

- More problems
- Further analysis/optimisation

Contributions
-------------

Please feel free to submit an issue or pull request for any bugs you may find or algorithms incorrectly implemented.

License
-------
GNU GPLv3