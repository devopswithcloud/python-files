import threading
import time

t = threading.Thread(target=lambda:time.sleep(5))
t.start()

