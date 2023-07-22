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