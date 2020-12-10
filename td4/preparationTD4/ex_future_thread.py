import time
import math
import concurrent.futures


def sqrt(n):
    time.sleep(1)
    return math.sqrt(n)


with concurrent.futures.ThreadPoolExecutor(max_workers = 4) as pool:
    l=[0, 1, 10, 100, 1000]
    print("*** Assynchronous future submit")
    futures = [pool.submit(sqrt, x) for x in l]
    print(futures)
    for x in futures:
        print(x.result())




