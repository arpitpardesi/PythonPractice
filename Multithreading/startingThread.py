from threading import Thread
from time import sleep


def my_function(arg, n):
    for i in range(arg):
        print(f"child Thread running {i} {n} ")
        sleep(0.5)


thread = Thread(target=my_function, args=(5,'A',))
thread.start()

thread = Thread(target=my_function, args=(10,'B',))
thread.start()
thread.join()

print("\nthread finished...exiting")

print('-----------------------------')
import threading
import time

class MyThread(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      print("Starting " + self.name)
      print_time(self.name, self.counter)
      print("Exiting " + self.name)

def print_time(threadName, counter):
   while counter:
      time.sleep(1)
      print("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)
thread3 = MyThread(3, "Thread-3", 3)

# Start new Threads
thread1.start()
thread3.start()

print("Exiting Main Thread")