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

stk = Stack()
inp = input('Enter Input : ').split(',')

for val in inp:
    val = [int(i) for i in val.split(' ')]
    while not stk.isEmpty():
        if val[0] <= stk.top()[0]:
                break
        print(stk.pop()[1])
    stk.push(val)