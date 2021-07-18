#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math


def check_prime(number):
    """
    为了更好地理解高性能编程的要素，让我们来看一段用于判断质数的简单代码样例
    """
    sqrt_number = math.sqrt(number)
    number_float = float(number)
    for i in range(2, int(sqrt_number) + 1):
        if (number_float / i).is_integer():
            return False
    return True


if __name__ == '__main__':
    print("check_prime(10000000) = ", check_prime(10000000))  # False
    print("check_prime(10000019) = ", check_prime(10000019))  # True
