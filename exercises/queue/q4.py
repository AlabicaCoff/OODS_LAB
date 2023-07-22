class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0
    
    def front(self):
        if self.is_empty():
            return None
        return self.items[0]
    
    def rear(self):
        if q.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)
    
class Customer:
    id = 1
    def __init__(self, walk_in, time):
        self.id = Customer.id
        self.walk_in = walk_in
        self.time = time
        Customer.id += 1
    
print(" ***Cafe***")
q = Queue([Customer(data.split(",")[0], data.split(",")[1]) for data in input("Log : ").split("/")])

b1, b2 = Queue(), Queue()
clk = 0
t1, t2 = 0, 0
waiting = []
dis_lst = []

while not q.is_empty() or not b1.is_empty() or not b2.is_empty():
    if b1.is_empty() and q.front() != None and clk >= int(q.front().walk_in):
        b1.enqueue(q.dequeue())

    if b2.is_empty() and q.front() != None and clk >= int(q.front().walk_in):
        b2.enqueue(q.dequeue())

    if not b1.is_empty():
        t1 += 1
        if t1 == int(b1.front().time):
            dis_lst.append([clk + 1, b1.front().id])
            waiting.append([clk + 1 - int(b1.front().time) - int(b1.front().walk_in), b1.front().id])
            b1.dequeue()
            t1 = 0

    if not b2.is_empty():
        t2 += 1
        if t2 == int(b2.front().time):
            dis_lst.append([clk + 1, b2.front().id])
            waiting.append([clk + 1 - int(b2.front().time) - int(b2.front().walk_in), b2.front().id])
            b2.dequeue()
            t2 = 0
    clk += 1

for i in sorted(dis_lst):
    print(f"Time {i[0]} customer {i[1]} get coffee")

if waiting != []:
    waiting.sort()
    if waiting[-1][0] == 0: 
        print("No waiting")
    else:
        print(f"The customer who waited the longest is : {waiting[-1][1]}") 
        print(f"The customer waited for {waiting[-1][0]} minutes")