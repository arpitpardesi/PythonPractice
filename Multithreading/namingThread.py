import threading
from threading import Thread

def func(x):
    print(f"current Thread: {threading.current_thread().name} {x}")

# Create thread objects
t1 = Thread(target=func, args=(2,), name='Thread-1')
t2 = Thread(target=func, args=(3,), name='Thread-2')

t1.start()
t2.start()

def my_function_1(arg):
   threading.current_thread().name = "custom_name"
   print("This tread name is", threading.current_thread().name)

# Create thread objects
thread1 = Thread(target=my_function_1, name='My_thread', args=(2,))
thread2 = Thread(target=my_function_1, args=(3,))

print("This tread name is", threading.current_thread().name)

# Start the first thread and wait for 0.2 seconds
thread1.start()
thread1.join()