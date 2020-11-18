"""
IPC client implemented to be used as a demonstration along with a multithreaded server script
"""

# pylint: disable=c-extension-no-member
import os
import sys
import sysv_ipc

KEY = 0x80


def user():
    """
    Gets a valid input from a user
    :return: 1 or 2 as an int
    """
    answer = 0
    while answer not in [1, 2]:
        print("1. to get current date/time")
        print("2. to terminate time server")
        answer = int(input())
    return answer


if __name__ == "__main__":
    try:
        message_queue = sysv_ipc.MessageQueue(KEY)
    except sysv_ipc.ExistentialError:
        print("Cannot connect to message queue", KEY, ", terminating.")
        sys.exit(1)

    REQUEST = user()

    if REQUEST == 1:
        pid = os.getpid()
        MESSAGE = str(pid).encode()
        message_queue.send(MESSAGE)
        MESSAGE, REQUEST = message_queue.receive(type=(pid + 3))
        response = MESSAGE.decode()
        print("Server response:", response)

    if REQUEST == 2:
        MESSAGE = b""
        message_queue.send(MESSAGE, type=2)
