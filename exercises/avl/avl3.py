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

    def insert_complete(self, lst, n, q = []):
        if len(lst) != (n // 2) + 1:
            return
        if q == []:
            new_lst = [0 for i in range(1, n // 2 + 1)] + lst
            cur = Node(new_lst.pop(0))
            self.root = cur
            q.append(cur)
        while q and new_lst:
            left = Node(new_lst.pop(0))
            right = Node(new_lst.pop(0))
            n = q.pop(0)
            n.left = left
            n.right = right
            q.append(left)
            q.append(right)
        return self.root
    
    def slash_tree(self, cur, less = 0):
        if cur and cur.left and cur.right:
            self.slash_tree(cur.left, min)
            self.slash_tree(cur.right, min)
            less = min(cur.left.data, cur.right.data)
            cur.data = less
            cur.left.data -= less
            cur.right.data -= less

    def sum_nodes(self):
        all_nodes = self.InOrder(self.root)
        return sum(all_nodes)
        
    def InOrder(self, cur, arr = []):
        if cur != None:
            self.InOrder(cur.left, arr)
            arr.append(cur.data)
            self.InOrder(cur.right, arr)
        return arr

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = input('Enter Input : ').split('/')
n = int(inp[0])
vals = [int(i) for i in inp[1].split()]
root = T.insert_complete(vals, n)
if root is None:
    print("Incorrect Input")
    exit(0)
T.slash_tree(root)
print(T.sum_nodes())