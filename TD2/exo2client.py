"""
IPC client
"""

# pylint: disable=no-name-in-module
import sys
from sysv_ipc import MessageQueue, ExistentialError

if __name__ == "__main__":
    KEY = 128

    try:
        mq = MessageQueue(KEY)
    except ExistentialError:
        print("IPC queue doesn't exist")
        sys.exit(1)

    while True:
        message_type = input("1 for time 2 to stop : ")
        if message_type.isdigit() and message_type in ["1", "2"]:

            mq.send("", type=int(message_type))
            print(f"send type {message_type}")
            if message_type == "1":
                message_type, t = mq.receive(type=3)
                print(message_type)
            else:
                print("server stopped")
                break
        else:
            print("bad input")
