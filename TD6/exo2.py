import time
from random import randint
from threading import Semaphore, Lock, Thread

THINKING = 1
HUNGRY = 2
EATING = 3

class State:
    def __init__(self):
        self.state = THINKING


N = 5
state = [State() for _ in range(N)]
sem = [Semaphore(0) for _ in range(N)]
lock = Lock()  # to restrain access to state array


def philosopher(i):
    while True:
        think()

        lock.acquire()

        state[i].state = HUNGRY

        # eat
        if (state[(i + N - 1) % N].state != EATING) and (state[(i + 1) % N] != EATING):
            state[i].state = EATING
            # block both neighbours
            sem[i].acquire()
            eat()

            sem[(i + N - 1) % N].release()
            sem[(i + 1) % N].release()

        sem[i].release()

        state[i].state = THINKING


def think():
    time.sleep(randint(1, 1000) / 1000)


def eat():
    time.sleep(randint(1, 1000) / 1000)


if __name__=="__main__":
    threads = [Thread(target=philosopher, args=(i,)) for i in range(N)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
