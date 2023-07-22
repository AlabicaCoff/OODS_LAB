class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0
    
    def front(self):
        return self.queue[0]
    
    def rear(self):
        return self.queue[-1]

    def size(self):
        return len(self.queue)
    
inp = [ch for ch in input("Enter people : ")]

q1 = Queue()
q2 = Queue()
q3 = Queue()

for ch in inp:
    q1.enqueue(ch)

time = 1
q2_timer, q3_timer = 0, 0
while not q1.is_empty():
    if not q2.is_empty():
        q2_timer += 1
        if q2_timer == 3:
            q2.dequeue()
            q2_timer = 0
            
    if not q3.is_empty():
        q3_timer += 1
        if q3_timer == 2:
            q3.dequeue()
            q3_timer = 0
        
    if q2.size() < 5:
        q2.enqueue(q1.dequeue())
    else:
        q3.enqueue(q1.dequeue())

    print(f"{time} {q1.queue} {q2.queue} {q3.queue}")
    time += 1