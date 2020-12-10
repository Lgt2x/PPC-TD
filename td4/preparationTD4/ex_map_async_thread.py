import time
import math
import concurrent.futures
 
def sqrt(n):
    time.sleep(2)
    return math.sqrt(n)

with concurrent.futures.ThreadPoolExecutor(max_workers = 4) as pool:
    l = [0, 1, 10, 100, 1000]
    print("*** Assynchronous thread map")
    res = pool.map(sqrt, l)
    print(res)
    for x in res:
        print(x)




