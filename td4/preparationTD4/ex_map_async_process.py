import time
import math
import multiprocessing


def sqrt(n):
    time.sleep(1)
    return math.sqrt(n)


if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        l = [0, 1, 10, 100, 1000]
        print("*** Assynchronous proces map")
        res = pool.map_async(sqrt, l)
        print(res)
        for x in res.get():
            print(x)
