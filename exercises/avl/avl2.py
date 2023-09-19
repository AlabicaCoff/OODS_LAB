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

    def search_node(self, data, cur):
        if cur is None or cur.data == data:
            return cur
        if cur.data > data:
            return self.search_node(data, cur.left)
        return self.search_node(data, cur.right)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
        self.printTree(self.root)
        print(50 * '-')
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

    def closestValue(self, root, value):
        close = root
        return self._closestValue(root, value, close)
        
    def _closestValue(self, root, value, close):
        if root is None:
            return close
        elif value == root.data:
            return value
        
        close_diff, root_diff = abs(close.data - value), abs(root.data - value)
        if (root_diff == close_diff and root.data > close.data) or (root_diff < close_diff):
            close = root

        if value < root.data:
            return self._closestValue(root.left, value, close)
        elif value > root.data:
            return self._closestValue(root.right, value, close)
        
            
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
            
T = BST()
inp = input('Enter Input : ').split('/')
inp, val = [int(i) for i in inp[0].split()], int(inp[1])
for i in inp:
    root = T.insert(i)
print(f"Closest value of {val} : {T.closestValue(root, val)}")