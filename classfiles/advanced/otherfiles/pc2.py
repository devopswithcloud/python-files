import multiprocessing
import time

def cpu_heavy_task():
    count =0
    for _ in range(10**7):
        count +=1

start = time.time()
p1 =multiprocessing.Process(target=cpu_heavy_task)
p2 =multiprocessing.Process(target=cpu_heavy_task)

p1.start();p2.start()
p1.join();p2.join()
end =time.time()

print(f"Time taken:{end-start:.2f}seconds")       