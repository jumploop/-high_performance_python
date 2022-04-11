#!/usr/bin/env python
# -*- coding:utf-8 -*-
import timeit
from itertools import islice


def fibonacci():
    i, j = 0, 1
    while True:
        yield j
        i, j = j, i + j


def fibonacci_naive():
    """
    5000 以内的斐波那契数中有几个奇数？
    :return:count
    """
    i, j = 0, 1
    count = 0
    while j < 5000:
        if j % 2 == 0:
            count += 1
        i, j = j, i + j
    return count


def fibonacci_transform():
    """
    5000 以内的斐波那契数中有几个奇数？
    :return: count
    """
    count = 0
    for f in fibonacci():
        if f > 5000:
            break
        if f % 2 == 0:
            count += 1
    return count


def fibonacci_succinct():
    """

    :return:
    """
    is_odd = lambda x: x % 2
    first_5000 = islice(fibonacci(), 0, 5000)
    return sum(1 for x in first_5000 if is_odd(x))


if __name__ == '__main__':
    setup = "from __main__ import " "(fibonacci, fibonacci_naive, fibonacci_transform, fibonacci_succinct)"
    iterations = 1000

    t = timeit.timeit(stmt="fibonacci_naive()", setup=setup, number=iterations)
    print(
        f"fibonacci_naive took {t / iterations:.5e}s to calculate 5000 fibonacci numbers"
    )

    t = timeit.timeit(stmt="fibonacci_transform()", setup=setup, number=iterations)
    print(
        f"fibonacci_transform took {t / iterations:.5e}s to calculate 5000 fibonacci numbers"
    )

    t = timeit.timeit(stmt="fibonacci_succinct()", setup=setup, number=iterations)
    print(
        f"fibonacci_succinct took {t / iterations:.5e}s to calculate 5000 fibonacci numbers"
    )
