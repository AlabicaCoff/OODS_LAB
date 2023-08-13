class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.sec_link = link()

    def __str__(self):
        return str(self.data)
    
class Snode(Node):
    def __init__(self, data):
        super().__init__(data)

class link:
    def __init__(self, head = None):
        if head is None:
            self.head = self.tail = None
        else:
            self.head = head
            cur = self.head
            while cur.next:
                cur = cur.next
            self.tail = cur
    
    def isEmpty(self):
        return self.head == None

    def next_node(self, n):
        if self.isEmpty():
            self.head = self.tail = n
        elif not isinstance(self.search(n.data), Node):
            self.tail.next = n
            self.tail = self.tail.next
    
    def search(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None
    
    def next_secondary_node(self, n, sn):
        pri_node = self.search(n)
        if pri_node != None:
            pri_node.sec_link.next_node(sn)

    def show_all(self):
        cur = self.head
        while cur:
            sec_cur = cur.sec_link.head
            print(f"{cur} : ", end='')
            while sec_cur:
                print(sec_cur, end=',')
                sec_cur = sec_cur.next
            print('')
            cur = cur.next

inp = input("input : ").split(",")
l = link()
for i in inp:
    u = i.split(" ")
    if u[0] == "ADN":
        l.next_node(Node(u[1]))
    elif u[0] == "ADSN":
        h = u[1].split("-")
        l.next_secondary_node(h[0],Snode(h[1]))
l.show_all()