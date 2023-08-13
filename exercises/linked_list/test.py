class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    
class LinkedList:
    def __init__(self, head = None):
        if head is None:
            self.head = self.tail = None
        else:
            self.head = head
            cur = self.head
            while cur.next:
                cur = cur.next
            self.tail = cur

    def __str__(self):
        if self.isEmpty():
            return ""
        cur, s = self.head, []
        while cur:
            s.append(str(cur.data))
            cur = cur.next
        return " -> ".join(s)

    def isEmpty(self):
        return self.head == None
    
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
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def add_head(self, item):
        node = Node(item)
        if self.isEmpty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
    
    def index(self, item):
        cur = self.head
        i = 0
        while cur:
            if cur.data == item:
                return i
            cur = cur.next
            i += 1
        return -1
    
    def pop(self, item):
        cur = self.head
        while cur:
            if cur.data == item:
                return cur
            cur = cur.next
        return None
    
    def search(self, index):
        if index >= self.size() or self.isEmpty():
            return None
        else:
            i = 0
            cur = self.head
            while cur:
                if index == i:
                    return cur
                cur = cur.next
                i += 1

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next