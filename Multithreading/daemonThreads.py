import threading
import time
from threading import Thread

def func(x, n):
    # print("Curent Thread Details:")
    for i in range(x):
        print(f"Running {i} {n} {threading.current_thread().daemon}")
        time.sleep(0.5)

t1 = Thread(target=func, args = (2,"A"), daemon=True)
t2 = Thread(target=func, args = (3,"B"))

t1.start()
t1.join()

t2.start()
t2.join()