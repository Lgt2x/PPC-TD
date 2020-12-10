"""
Process pool demonstration, with both async and sync methods
"""

import multiprocessing.pool
from random import randint
from sys import argv
from time import time


def is_prime(number):
    """
    Checks if a given number is prime
    :param number: the number given to verify primality
    :return: True if prime, False otherwise
    """
    if number <= 3:
        return number > 1
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i = i + 6
    return True


if __name__ == "__main__":
    # ASYNC
    start_async = time()
    print("Workers : ", argv[1])

    with multiprocessing.Pool(processes=int(argv[1])) as pool:
        number_list = [randint(10 ** 3, 10 ** 6) for _ in range(10 ** 6)]
        print("*** Asynchronous proces map")
        res = pool.map_async(is_prime, number_list)

    print(time() - start_async)
    print()

    # SYNC
    start_sync = time()

    with multiprocessing.Pool(processes=int(argv[1])) as pool:
        number_list = [randint(10 ** 3, 10 ** 6) for _ in range(10 ** 6)]
        print("*** Synchronous proces map")
        res = pool.map(is_prime, number_list)

    print(time() - start_sync)
