#!/usr/bin/env python3

"""
Basic example of pipes to reverse a string in a child process
"""

from multiprocessing import Process, Pipe


def reversing(conn):
    """
    Used a child process, sends in a pipe a reversed version of the string
    from this pipe
    :param conn: the pipe
    """
    # Send reversed sring from pipe into pipe (blocking send)
    conn.send(conn.recv()[::-1])

    # Close connexion afterwards
    conn.close()


if __name__ == '__main__':
    # Initiate Pipe
    parent_conn, child_conn = Pipe()

    # Create child process
    child_process = Process(target=reversing, args=(child_conn,))

    # Send stdin input into pipe
    parent_conn.send(input("Type a string to be reversed : "))

    # Start the child process
    child_process.start()

    # Print received input from pipe
    print("String reversed is : ", parent_conn.recv())

    # Wait for the child process to end
    child_process.join()
