- ex_map.py
Example of simple map (map function on list)

- ex_map_process.py
Example of multiprocessing.map (Synchronous map using processes)
the map waits until all processes have finished

- ex_map_async_process.py
Example of multiprocessing.map_assync (Assynchronous map using processes)
the "print(res)" does not wait the end of submited processes to appear, the map is "assynchonous" and returns a "MapResult" which deliver results when the "get()" function is applied.

- ex_map_async_thread.py
Assynchronous map for thread
same thing as previous one, but for threads instead of processes, using concurrent.futures.ThreadPoolExecutor
I intendendly called "pool" the executor to illustrate the similarities process/thread
The ThreadPoolExecutor.map corresponds to multiprocessing.map_async
The "print(res)" also executes immediatly
The 'get' is replaced by effective accesses: the "print(x)" are executed as soon as x (=res[i]) is available.
As there are only 4 threads, and that tasks are submit 4 by 4 (?), there is a 2seconds delay after the four first results are printed.

- ex_future_thread.py
example of concurrent.futures
The "pool.submit" launchs a thread to execute the function and returns a handle on the running execution. This handle is called a "Future" in python.
When the Future object is accessed, if the corresponding thread execution is not finished, python stalls until the execution finishes. If the execution is finished the Future object is the result of the execution.
Again, a sleep can be observed because there are only 4 threads used.
