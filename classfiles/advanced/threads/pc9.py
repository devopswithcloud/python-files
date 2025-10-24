# to show race condtion comment with counter.get_lock()
from multiprocessing import Process, Value

def increment(counter):
    for _ in range(100000):
    #with counter.get_lock():   
            counter.value += 1

if __name__ == "__main__":
    counter = Value('i', 0)
    p1 = Process(target=increment, args=(counter,))
    p2 = Process(target=increment, args=(counter,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Final counter value:", counter.value)