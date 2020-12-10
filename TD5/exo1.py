"""
Lock demonstration to use a shared variable
"""

import sys
import threading
from multiprocessing import pool
from random import random


def count_points_in(nb_pts):
    """
    Puts in a locked counter the of points in a circle of radius 1
    :param nb_pts: number of points
    """
    print("Starting thread:", threading.current_thread().name)

    nb_in = 0

    for _ in range(nb_pts):
        if random()**2 + random()**2 < 1:
            nb_in += 1

    global total_points

    with lock:
        print("lock acquired")
        total_points += nb_in

    print("Stopping thread", threading.current_thread().name)


if __name__ == "__main__":
    # Declaring lock and shared number of points
    lock = threading.Lock()
    total_points = 0

    print(f"Starting thread {threading.current_thread().name}")

    pts_thread = int(sys.argv[1])  # First argument : number of points by thread
    nb_thread = int(sys.argv[2])  # Second argument : number of threads

    print(f"Start {nb_thread} with {pts_thread} points each")

    # Create a thread pool and execute nb_thread times
    pool = pool.ThreadPool(processes=nb_thread)
    pool.map_async(count_points_in, [pts_thread]*nb_thread).get()

    print(total_points)

    with lock:
        print(4 * total_points / pts_thread / nb_thread)
        print(f"Ending thread {threading.current_thread().name}")
