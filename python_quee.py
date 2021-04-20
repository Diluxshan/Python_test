import queue

q1 = queue.Queue(5)
q1.put(1)
q1.put(2)
q1.put(3)
q1.put(4)
q1.put(5)
print(q1.full())
print(q1.qsize())