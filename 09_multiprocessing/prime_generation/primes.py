import math
import time


def check_prime(n):
    if n % 2 == 0:
        return False
    return all(n % i != 0 for i in range(3, int(math.sqrt(n)) + 1, 2))


if __name__ == "__main__":
    t1 = time.time()
    #number_range = xrange(100000000, 100010000)  # A
    #number_range = xrange(100000000, 100100000)  # B
    number_range = range(100000000, 101000000)  # C
    primes = [
        possible_prime
        for possible_prime in number_range
        if check_prime(possible_prime)
    ]

    print("Took:", time.time() - t1)
    print(len(primes), primes[:10], primes[-10:])
