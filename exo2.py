#!/usr/bin/env python3

"""
An example of message passing between processes using signals
"""

import signal
from multiprocessing import Process
from time import sleep
from os import kill, getppid, getpid


def pidprint(*args, **kwargs):
    """
    print function wrapped to display pid ahead
    """
    print(getpid(), end=" ")
    print(*args, **kwargs)


def wait():
    """
    Function called as the child process
    """
    pidprint("Child started, init sleep")
    sleep(5)
    pidprint("Sleep ended, sending signal to parent")
    kill(getppid(), signal.SIGINT)  # Send a signal to parent


def handler(_, _2):
    """
    Signal handler, for the parent process
    """
    pidprint("Received signal")
    child.kill()
    pidprint("Killed child")


if __name__ == "__main__":
    child = Process(target=wait)
    child.start()
    pidprint("Starting child process")

    signal.signal(signal.SIGINT, handler)  # Listen for sigint in main process
    child.join()

    pidprint("Child terminated")
