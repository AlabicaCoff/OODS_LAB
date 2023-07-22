class Stack:
    def __init__(self):
        self.lst = []

    def size(self):
        return len(self.lst)
    
    def peek(self):
        return self.lst[-1]

    def is_empty(self):
        if len(self.lst) == 0:
            return True
        else:
            return False
    
    def pop(self):
        if not self.is_empty():
            return self.lst.pop()

    def push(self, item):
        self.lst.append(item)

plt_data = [inp.split(" ") for inp in input("Enter Input : ").split(",")]

s = Stack()

w, f = 0, 1 # w = weight, f = frequency

for plt in plt_data:
    if plt_data.index(plt) == 0:
        s.push(plt)
        continue
    elif int(s.peek()[w]) >= int(plt[w]):
        s.push(plt)
        continue
    while int(s.peek()[w]) < int(plt[w]):
        print(s.pop()[f])
        if s.is_empty():
            s.push(plt)
        elif int(s.peek()[w]) >= int(plt[w]):
            s.push(plt)
        elif s.size() < 1:
            break