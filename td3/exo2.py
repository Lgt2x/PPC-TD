"""
Demonstration of task parallelism with threads and queues
"""

from sys import stdin
import threading
from queue import Queue
import statistics


def stats(data_q, stats_q, data_flag, stat):
    """
    Computes statistics from data of a queue when an event is triggered, outputs to a queue
    :param data_q: Queue where data comes from
    :param stats_q: Queue where result goes
    :param data_flag: Event which triggers the computation
    :param stat: tuple of the form (module, function) which represents the function to be called
    """

    print("Starting thread:", threading.current_thread().name)

    data_flag.wait()  # Wait for the event
    base_data = data_q.get()  # Get data from Queue
    # Put result in output queue
    stats_q.put(stat[1]
                + " : "
                + str(getattr(stat[0], stat[1])(base_data)))

    print("Ending thread:", threading.current_thread().name)


if __name__ == "__main__":
    print("Starting thread:", threading.current_thread().name)

    data_queue = Queue()  # Queue for sending data to threads
    stats_queue = Queue()  # Queue to get data from threads
    data_ready = threading.Event()  # Notifies the threads that data is ready to be served

    # Tuples to be passed to thread function which call these functions
    methods = [(__builtins__, "min"),
               (__builtins__, "max"),
               (statistics, "median"),
               (statistics, "mean"),
               (statistics, "stdev")]

    # Thread array
    threads = [threading.Thread(target=stats,
                                args=(data_queue, stats_queue, data_ready, method))
               for method in methods]

    # Start all threads
    for thread in threads:
        thread.start()

    # Get data from stdin until EOF
    data = []
    input_str = stdin.read().split()
    for s in input_str:
        try:
            x = float(s)
        except ValueError:
            print("bad number", s)
        else:
            data.append(x)

    # Put data in queue enough times for all threads to get a copy of the data
    for _ in range(len(methods)):
        data_queue.put(data)
        data_ready.set()

    # Wait for all threads
    for thread in threads:
        thread.join()
        print(stats_queue.get())

    print("Ending thread:", threading.current_thread().name)
