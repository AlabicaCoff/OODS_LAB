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

def match_paren(a, b):
    open_paren = "([{"
    close_paren = ")]}"
    if a in open_paren and b in close_paren:
        return open_paren.index(a) == close_paren.index(b)
    elif b in open_paren and a in close_paren:
        return open_paren.index(b) == close_paren.index(a)

stack = Stack()
strr = input("Enter Input : ")

for ch in strr:
    if not stack.is_empty() and match_paren(stack.peek(), ch):
        stack.pop()
    elif ch in '([{' or ch in ')]}':
        stack.push(ch)

if stack.size() == 0:
    print("Parentheses : Matched ! ! !")
else:
    print("Parentheses : Unmatched ! ! !")