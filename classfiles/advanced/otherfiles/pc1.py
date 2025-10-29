import threading
import time 

def cpu_heavy_task():
    count=0
    for _ in range(10**7):
        count +=1

start = time.time()
t1 =threading.Thread(target=cpu_heavy_task)
t2 =threading.Thread(target=cpu_heavy_task)

t1.start();t2.start()
t1.join();t2.join()
end =time.time()

print(f"Time taken:{end-start:.2f}seconds")