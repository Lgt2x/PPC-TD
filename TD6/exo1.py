N = 5
chopstick = [Mutex() for i in range(N)]


def philosopher(i):
    while True:
        think()

        left_stick = i
        right_stick = (i + 1) % N

        if i!=4:
            chopstick[left_stick].acquire()
            chopstick[right_stick].acquire()
        else:
            chopstick[right_stick].acquire()
            chopstick[left_stick].acquire()

        eat()

        chopstick[left_stick].release()
        chopstick[right_stick].release()


def think():
    pass


def eat():
    pass
