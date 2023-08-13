class Stack():
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        
    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

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
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)
    
    def reverseK(self, k):
        q = Queue()
        s = Stack()
        for i in range(k):
            s.push(self.dequeue())
        for j in range(k):
            q.enqueue(s.pop())
        while not self.is_empty():
            q.enqueue(self.dequeue())
        self.items += q.items
        return self.items