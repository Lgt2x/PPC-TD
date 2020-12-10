#!/usr/bin/env python3

"""
An exemple of shared memory between processes
"""

from multiprocessing import Process, Manager
from sys import argv


def fib(number, fib_list):
    """
    Returns the #num fibonacci number using recursion
    :param number: current number
    :param fib_list: pointer to shared list of fibonacci numbers
    """

    # If the number has already been computed
    if fib_list[number] != -1:
        return fib_list[number]

    if number <= 1:
        fib_list[number] = number
    else:
        fib_list[number] = fib(number - 1, fib_list) + fib(number - 2, fib_list)

    return fib_list[number]


if __name__ == "__main__":
    if len(argv) == 2 and argv[1].isdigit() and int(argv[1]) >= 0:
        with Manager() as manager:
            num = int(argv[1])
            fibs = manager.list([-1]*(num+1))
            p = Process(target=fib, args=(num, fibs))
            p.start()
            p.join()

            print(fibs)
