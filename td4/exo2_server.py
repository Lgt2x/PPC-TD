"""
Example of an IPC server providing date information to a client
"""

# pylint: disable=no-name-in-module
import concurrent.futures
from time import asctime
from sysv_ipc import MessageQueue, IPC_CREX


def datetime_request(queue, pid):
    """
    Handles a time request asynchronously
    :param queue: the queue to send the date back into
    :param pid: the request client pid
    """
    time = asctime().encode()
    queue.send(time, type=(int(pid) + 3))
    print(f"date {time} sent to client {pid}")


if __name__ == "__main__":
    # Create IPC with key 0x80 if it doesn't exist
    KEY = 0x80
    message_q = MessageQueue(KEY, IPC_CREX)

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        while True:
            message, message_type = message_q.receive()

            # 1 : date request
            if message_type == 1:
                # Do it async
                pool.submit(datetime_request, message_q, message)
            # 2 : stop request
            elif message_type == 2:
                print("terminating")
                message_q.remove()
                break
