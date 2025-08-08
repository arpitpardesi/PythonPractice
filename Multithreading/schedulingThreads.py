import threading
import time


def my_function(arg):
    print(f"Thread {threading.current_thread().name} running with arg: {arg}")
    for i in range(arg):
        print(f"{threading.current_thread().name} processing {i}")


# Start time
start = time.time()
print('START:', time.ctime(start))
# Create thread objects with names
t1 = threading.Timer(5, my_function, args=(5,))
t1.start()

# Wait for the thread to complete
t1.join()
print('END:', time.ctime(time.time()))
print('Total time taken:', time.time() - start)
print("Main Thread Finished...")