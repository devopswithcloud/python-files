# thread synchronization to avoid race condition
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1_000_000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(10)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Final counter value:", counter)
