import time
import threading

def worker():
    time.sleep(2)
    print("worker finised")

t = threading.Thread(target=worker)

t.start()
print(t.is_alive())
print(t.ident)

t.join()
print(t.is_alive())
print("Main thread continues")
    