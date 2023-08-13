class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next

class LinkedList:
    def __init__(self, head = None):
        if head is None:
            self.head = None
        else:
            self.head = head

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, ""
        while cur:
            s += str(cur.data) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None
    
    def tail(self):
        cur = self.head
        while cur.next:
            cur = cur.next
        return cur

    def size(self):
        cur = self.head
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next
        return cnt

    def append(self, item):
        node = Node(item)
        if self.isEmpty():
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def add_head(self, item):
        node = Node(item)
        if self.isEmpty():
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def search(self, item):
        if self.isEmpty():
            return f"Not Found {item} in"
        else:
            cur = self.head
        while cur:
            if cur.data == item:
                return f"Found {item} in"
            cur = cur.next
        return f"Not Found {item} in"
    
    def index(self, item):
        cur = self.head
        i = 0
        while cur:
            if cur.data == item:
                return i
            cur = cur.next
            i += 1
        return -1

    def pop(self, pos):
        if pos > self.size() or pos < -self.size() or self.isEmpty():
            return "Out of Range"
        elif pos >= 0:
            i = 0
            cur = self.head
            while cur:
                if pos == 0:
                    self.head = self.head.next
                    return "Success"
                if pos - 1 == i:
                    cur.next = cur.next.next
                    return "Success"
                cur = cur.next
                i += 1
            return "Out of Range"
        elif pos < 0:
            i = - self.size()
            cur = self.head
            while cur:
                if pos <= -self.size():
                    self.head = self.head.next
                    return "Success"
                if pos - 1 == i:
                    cur.next = cur.next.next
                    return "Success"
                cur = cur.next
                i += 1
            return "Out of Range"
                

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.add_head(i[3:])
    elif i[:2] == "SE":
        print("{0} {1}".format(L.search(i[3:]), L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)