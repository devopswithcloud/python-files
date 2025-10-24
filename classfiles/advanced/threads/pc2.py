import threading

class MyThread(threading.Thread):
    def run(self):
        print("custom thread running")

t = MyThread()
t.start()
t.join(timeout=5)
print("Completed")