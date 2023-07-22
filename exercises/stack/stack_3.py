class Stack:
    def __init__(self):
        self.lst = []

    def size(self):
        return len(self.lst)
    
    def peek(self):
        if not self.is_empty():
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

def get_priority(op):
    
    if op in '+-':
        return 1
    elif op in '*/':
        return 2
    elif op in '^':
        return 3
    
def infix2postfix(exp) :
    s = Stack()
    postfix = ""

    for ch in exp:
        if ch.isalpha():
            postfix += ch
        elif ch in '+-*/(^':
            if s.is_empty():
                s.push(ch)
            elif (s.peek() in '+-*/' and ch == '(') or (s.peek() == '(' and (ch in '+-*/^' or ch == '(')) or get_priority(s.peek()) < get_priority(ch):
                s.push(ch)
            else:
                while get_priority(s.peek()) >= get_priority(ch):
                    postfix += s.pop()
                    if s.is_empty() or s.peek() == '(':
                        break
                s.push(ch)
        elif ch == ')':
            while s.peek() != '(':
                postfix += s.pop()
            s.pop()

    while not s.is_empty():
        postfix += s.pop()
    return postfix

inp = input("Enter Infix : ")
print(f"Postfix : {infix2postfix(inp)}")
