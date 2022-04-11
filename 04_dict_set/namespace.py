#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
from math import sin


def test1(x):
    """
    >>> %timeit test1(123_456)
    162 µs ± 3.82 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    """
    return 1 + sum(math.sin(x) for _ in range(1000))


def test2(x):
    """
    >>> %timeit test2(123_456)
    124 µs ± 6.77 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    """
    return 1 + sum(sin(x) for _ in range(1000))


def test3(x, sin=math.sin):
    """
    >>> %timeit test3(123_456)
    105 µs ± 3.35 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    """
    return 1 + sum(sin(x) for _ in range(1000))
