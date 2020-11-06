"""
Example of an IPC server providing date information to a client
"""

# pylint: disable=no-name-in-module
from time import asctime
from sysv_ipc import MessageQueue, IPC_CREX


if __name__ == "__main__":
    # Create IPC with key 0x80 if it doesn't exist
    KEY = 128
    mq = MessageQueue(KEY, IPC_CREX)

    while True:
        message, t = mq.receive()

        # 1 : date request
        if t == 1:
            message = asctime().encode()
            mq.send(message, type=3)
            print(f"date {message} sent")
        # 2 : stop request
        elif t == 2:
            print("terminating")
            mq.remove()
            break
