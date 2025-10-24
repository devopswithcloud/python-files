import threading
import time 

class MyThread(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name =name

    def run(self):
        for i in range(3):
            print(f"{self.name} executing step {i}")
            time.sleep(1)

t1 = MyThread("Custom Thread-1")
t1.start()
t1.join()