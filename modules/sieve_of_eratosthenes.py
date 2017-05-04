import math


def get_primes(n):
    sieve = [True] * n

    for i in range(2, int(math.sqrt(n))):
        for j in range(i * 2, n, i):
            sieve[j] = False
    return [num for num in range(2, n) if sieve[num]]
