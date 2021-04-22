import queue
import time
import datetime

q1 = queue.Queue(6)
q1.put(1)
q1.put(2)
q1.put(3)
q1.put(4)
q1.put(5)
print(q1.full())
print(q1.qsize())
print("Successfull finished")

for i in range (0,10):
    print(q1.qsize())
    time.sleep(1)

