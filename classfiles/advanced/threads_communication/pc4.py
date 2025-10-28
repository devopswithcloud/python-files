import threading

condition = threading.Condition()
data_ready = False

def producer():
    global data_ready
    with condition:
        print("Producter: preparing data")
        data_ready=True
        condition.notify() # wakes up waiting threads

def consumer():
    with condition:
        print("Consumer: waiting for data")
        condition.wait()
        if data_ready:
            print("Consumer : got data")

def consumer2():
    with condition:
        print("Consumer: waiting for data")
        condition.wait()
        if data_ready:
            print("Consumer2 : got data")

t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=producer)
t1.start()
t2.start()
t1.join()
t2.join()