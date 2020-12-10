"""
Thread pool demonstration calculating a pi approximation
"""

import sys
import threading
from multiprocessing import pool
from random import random


def proportion(nb_pts):
    """
    Returns a proportion of points in a circle of radius 1
    :param nb_pts: number of points
    :return: prop
    """
    print("Starting thread:", threading.current_thread().name)

    nb_in = 0

    for _ in range(nb_pts):
        if random()**2 + random()**2 < 1:
            nb_in += 1

    return nb_in


if __name__ == "__main__":
    print(f"Starting thread {threading.current_thread().name}")

    pts_thread = int(sys.argv[1])  # First argument : number of points by thread
    nb_thread = int(sys.argv[2])  # Second argument : number of threads

    print(f"Start {nb_thread} with {pts_thread} points each")

    as_result = [0]*nb_thread

    # Create a thread pool
    pool = pool.ThreadPool(processes=nb_thread)
    for i in range(nb_thread):
        # Each thread computes `pts_thread` points
        as_result[i] = pool.apply_async(func=proportion, args=(pts_thread,))

    sum_points_in = sum(as_result[i].get() for i in range(nb_thread))

    print(4 * sum_points_in / pts_thread / nb_thread)
    print(f"Ending thread {threading.current_thread().name}")
