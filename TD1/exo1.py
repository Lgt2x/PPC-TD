#!/usr/bin/env python3

"""
A simple demonstration of multiprocessing in Python
Computes fibonacci number in parallel, and demonstrates pid/ppid
"""

from os import getppid, getpid
from time import sleep
from multiprocessing import Process
from sys import argv


def fib(num, init):
    """
    Returns the #num fibonacci number using recursion
    :param num: current number
    :param init: initial value
    """
    sleep(num)
    if num <= 1:
        if num == init:
            print(num, end=" ")
            print(getpid(), getppid())
        return num
    if num == init:
        print(fib(num - 1, num) + fib(num - 2, num), end=" ")
        print(getpid(), getppid())
        return 0
    return fib(num - 1, num) + fib(num - 2, num)


if __name__ == "__main__":
    # use `watch -n 1 "ps -ax | grep exo1.py"` to display processes and pids
    if len(argv) == 2 and argv[1].isdigit() and int(argv[1]) >= 0:
        for i in range(int(argv[1])):
            p = Process(target=fib, args=(int(i), int(i)))
            p.start()
            p.join()
        print()
    else:
        print("invalid arguments")
