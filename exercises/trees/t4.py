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

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
        return self.root

    def _insert(self, data, cur):
        if data < cur.data:
            if cur.left is None:
                cur.left = Node(data)
            else:
                self._insert(data, cur.left)
        elif data >= cur.data:
            if cur.right is None:
                cur.right = Node(data)
            else:
                self._insert(data, cur.right)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def printTreeHeight(self, node, level = 0):
        if node == None:
            return level - 1
        else:
            left_height = self.printTreeHeight(node.left, level + 1)
            right_height = self.printTreeHeight(node.right, level + 1)
            return max(left_height, right_height)
        
    def InOrder(self, cur, arr = []):
        if cur != None:
            self.InOrder(cur.left, arr)
            arr.append(cur.data)
            self.InOrder(cur.right, arr)
        return arr
    
    def PreOrder(self, cur, arr = []):
        if cur != None:
            arr.append(cur.data)
            self.PreOrder(cur.left, arr)
            self.PreOrder(cur.right, arr)
        return arr
    
    def PostOrder(self, cur, arr = []):
        if cur != None:
            self.PostOrder(cur.left, arr)
            self.PostOrder(cur.right, arr)
            arr.append(cur.data)
        return arr
    
    def BFS(self, cur, q = [], arr = []):
        if q == []:
            q.append(cur)
        while q:
            n = q.pop(0)
            arr.append(n.data)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return arr
    
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print(f"Preorder : {' '.join(list(map(str, T.PreOrder(root))))}")
print(f"Inorder : {' '.join(list(map(str, T.InOrder(root))))}")
print(f"Postorder : {' '.join(list(map(str, T.PostOrder(root))))}")
print(f"Breadth : {' '.join(list(map(str, T.BFS(root))))}")
