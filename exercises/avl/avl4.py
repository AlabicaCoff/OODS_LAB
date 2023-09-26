def nameValue(val):
    return sum(bytearray(val, 'utf-8'))

class TreeNode(object):
    def __init__(self, data, left = None, right = None):
            self.data = data
            self.key = nameValue(data)
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()
        
    def __str__(self):
        return str(self.data)
        
    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a,b)
        return self.height
    
    def getHeight(self, node):
        if node is None:
            return -1
        return node.height
        
    def balanceValue(self):
        return self.getHeight(self.left) - self.getHeight(self.right)

class AVL_Tree(object):
    def __init__(self, root = None):
        if root is None:
            self.root = None
        self.root = root

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root

    def _insert(self, root, data):
        if root is None:
            return TreeNode(data)
        else:
            key = nameValue(data)
            if int(key) < int(root.key):
                root.left = self._insert(root.left, data)
            else:
                root.right = self._insert(root.right, data)
            root = self.getBalance(root)                
            return root

    def delete(self, data):
        self.root = self._delete(self.root, data)
        return self.root
  
    def _delete(self, root, data):
        if root is None: 
            return root
        key = nameValue(data)
        if int(key) < int(root.key):
            root.left = self._delete(root.left, data)
        elif int(key) > int(root.key):
            root.right = self._delete(root.right, data)
        else:
            if root.left is None or root.right is None:
                root = root.left if root.right is None else root.right
            else:
                temp = root.right
                while temp.left is not None:
                    temp = temp.left
                root.data, root.key = temp.data, nameValue(temp.data)
                root.right = self._delete(root.right, temp.data)
        root = self.getBalance(root)
        return root

    def rightRotate(self, x) :
        y = x.left
        x.left = y.right
        y.right = x
        x = y
        x.right.setHeight()
        x.setHeight()
        return x
    
    def leftRotate(self, x) :
        y = x.right
        x.right = y.left
        y.left = x    
        x = y
        x.left.setHeight()
        x.setHeight()
        return x

    def getHeight(self, root):
        if root is None:
            return -1
        return root.getHeight(root)

    def getBalance(self, x):
        if x == None:
            return x
        balance = x.balanceValue()
        if balance == -2:
            if x.right.balanceValue() == 1 :
                x.right = self.rightRotate(x.right)
            x = self.leftRotate(x)
        elif balance == 2: 
            if x.left.balanceValue() == -1:   
                x.left = self.leftRotate(x.left)                                         
            x = self.rightRotate(x)
        x.setHeight()
        return x 

    def getMinValueNode(self, root):
        ...

    def printTree(self, node, level = 0):
        if node != None:
            print(' ' * 4 * level + f"{node} ({node.key})")
            if node.left is None and node.right:
                print(' ' * 4 * (level + 1) + "*")
            self.printTree(node.left, level + 1)
            if node.right is None and node.left:
                print(' ' * 4 * (level + 1) + "*")
            self.printTree(node.right, level + 1)

    def printTree1(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
avl_tree = AVL_Tree()
root = None
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")
for i in inp:
    op, *data = i.split(" ")
    data = data[0] if data else ""
    if op == "I":
        root = avl_tree.insert(data)
    elif op == "D":
        root = avl_tree.delete(data)
    elif op == "P":
        avl_tree.printTree(root)
        print("------------------------------")