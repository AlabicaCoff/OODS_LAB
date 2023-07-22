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

def dec2bin(decnum):
    s = Stack()
    bi = ""

    while int(decnum) > 0:
        s.push(int(decnum % 2))
        decnum /= 2

    while not s.is_empty():
        bi += str(s.pop())
    return bi
        

print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))