# non thread synchronization with are not thread safe
import threading

counter = 0  # Shared resource

def increment():
    global counter
    for _ in range(100000):
        counter += 1  # Not thread-safe

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print("Final counter value:", counter)
