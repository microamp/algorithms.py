algorithms.py
=============

Python 3 port of [algorithms](https://github.com/sagivo/algorithms) by @sagivo for fun ~~and profit~~

Problems
--------

| Problem                                                                                                                                                                                   | Solution                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [Dijkstra's algorithm for finding the shortest path between two nodes](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)                                                              | dijkstra.py                |
| [Newton's method for finding the square root of a number](https://en.wikipedia.org/wiki/Newton%27s_method)                                                                                | sqrt.py                    |
| [Binary search algorithm](https://en.wikipedia.org/wiki/Binary_search_algorithm)                                                                                                          | binary_search.py           |
| [Longest increasing subsequence](http://en.wikipedia.org/wiki/Longest_increasing_subsequence)                                                                                             | lis.py                     |
| [Longest common subsequence](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)                                                                                            | lcs.py                     |
| [Quicksort](http://en.wikipedia.org/wiki/Quicksort)                                                                                                                                       | quicksort.py               |
| [Mergesort](https://en.wikipedia.org/wiki/Merge_sort)                                                                                                                                     | mergesort.py               |
| Mix and combine sets of cells to list all possible combinations                                                                                                                           | mix_sets.py                |
| [Finding all combinations of well-formed brackets](http://stackoverflow.com/questions/727707/finding-all-combinations-of-well-formed-brackets)                                            | well_formed_brackets.py    |
| [Phonewords](http://www.mobilefish.com/services/phonenumber_words/phonenumber_words.php)                                                                                                  | phonewords.py              |
| [Permutation](https://en.wikipedia.org/wiki/Permutation)                                                                                                                                  | permutation.py             |
| [Finding the power set of a given set](http://en.wikipedia.org/wiki/Power_set)                                                                                                            | power_set.py               |
| [Find the next higher number that has the same set of digits](http://stackoverflow.com/questions/9368205/given-a-number-find-the-next-higher-number-which-has-the-exact-same-set-of-digi) | same_digits_next_bigger.py |
| [Find the minimum insertions needed to form a Palindrome](from http://www.geeksforgeeks.org/dynamic-programming-set-28-minimum-insertions-to-form-a-palindrome/)                          | palindrome_insertions.py   |
| [Knuth–Morris–Pratt algorithm](http://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm)                                                                                 | kmp.py                     |
| [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)                                                                                                            | TODO                       |
| [Knapsack problem](http://en.wikipedia.org/wiki/Knapsack_problem)                                                                                                                         | TODO                       |

How to run tests
----------------

All tests are in 'tests.py'. Run the following command to test them.

```bash
python -m tests
```

Versions tested
---------------

- Python 3.4

TODO
----

- More problems
- Further optimisation

Additional notes
----------------

- Most solutions here are defined in terms of recursion despite of that it is not generally considered a good practice in Python (1). The focus here is more on the algorithms, rather than the language they are implemented in.
- Mutation of data structures was avoided as much as possible, but sometimes it is difficult to do in Python.

Notes:
1. Python is _not_ a functional programming language, and there is no TCO support in CPython after all.

Contributions
-------------

Please feel free to submit an issue or pull request for any bugs or incorrect implementations of the algorithms you may find.

License
-------
GNU GPLv3