# Deamon thread
import threading
import time

def background_task():
    while True:
        print("Running in background")
        time.sleep(2)


t =threading.Thread(target=background_task,daemon=True)
t.start()
time.sleep(5)
print("Main thread done")