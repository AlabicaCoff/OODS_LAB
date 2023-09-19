class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data, stk = []):
        if data in "+-*/" and len(stk) > 1:
            op = Node(data)
            op.right = stk.pop()
            op.left = stk.pop()
            stk.append(op)
        else:
            var = Node(data)
            stk.append(var)
        self.root = stk[0]
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def Infix(self, cur, arr = []):
        if cur != None:
            if cur.left:
                arr.append('(')

            self.Infix(cur.left, arr)
            arr.append(cur.data)
            self.Infix(cur.right, arr)

            if cur.right:
                arr.append(')')
        return arr

    def Prefix(self, cur, arr = []):
        if cur != None:
            arr.append(cur.data)
            self.Prefix(cur.left, arr)
            self.Prefix(cur.right, arr)
        return arr
            
T = BST()
stk = []
inp = input('Enter Postfix : ')
for i in inp:
    root = T.insert(i, stk)
print("Tree :")
T.printTree(root)
print("--------------------------------------------------")
print(f"Infix : {''.join(T.Infix(root))}")
print(f"Prefix : {''.join(T.Prefix(root))}")
