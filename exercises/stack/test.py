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

d= {'a':2,'b':5,'c':3, 'd':5}
o = {}
for k in d.keys():
    if d[k] == d[f'{max(d, key=d.get)}']:
        o[k] = d[k]
print(o)