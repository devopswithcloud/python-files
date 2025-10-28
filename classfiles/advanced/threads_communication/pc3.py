import threading
import time
event = threading.Event()

def waiter():
    print("Waiter :waiting for event")
    event.wait()# blocks until event.set() is called
    print("Waiter:event recieved")

def setter():
    time.sleep(2)
    print("Settersetting event")
    event.set()

t1 = threading.Thread(target=waiter)
t2 = threading.Thread(target=setter)

t1.start()
t2.start()
t1.join()
t2.join()