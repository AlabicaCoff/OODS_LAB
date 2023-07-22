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
            return -1
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

q = Queue()
inps = [ip for ip in input("Enter Input : ").split(',')]

for inp in inps:
    if inp[0] == 'E':
        q.enqueue(inp[2:])
        print(f"Add {inp[2:]} index is {q.items.index(inp[2:])}")
    elif inp[0] == 'D':
        if q.is_empty():
            print(q.dequeue())
        else:
            print(f"Pop {q.dequeue()} size in queue is {q.size()}")

if q.is_empty():
    print("Empty")
else:
    print(f"Number in Queue is :  {q.items}")