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

    def search_node(self, data):
        if data in dic.keys():
            return dic[data]

    def insert(self, parent, child):
        if self.root is None:
            dic[parent] = self.root = Node(parent)
            dic[child] = self.root.left = Node(child)
        else:
            pnode = self.search_node(parent)
            if not pnode.left:
                dic[child] = pnode.left = Node(child)
            else:
               dic[child] = pnode.right = Node(child)
        return self.root
    
    def top_view_left(self, cur, arr = []):
        if cur != None:
            self.top_view_left(cur.left, arr)
            arr.append(cur.data)
        return arr
    
    def top_view_right(self, cur, arr = []):
        if cur != None:
            arr.append(cur.data)
            self.top_view_right(cur.right, arr)
        return arr

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T, dic = BST(), {}
inp = input('Enter Input : ').split(',')
for i in inp:
    splited = i.split()
    parent, child = splited[0], splited[1]
    root = T.insert(parent, child)
print(f"Top view : {' '.join(T.top_view_left(root))} {' '.join(T.top_view_right(root.right))}")
