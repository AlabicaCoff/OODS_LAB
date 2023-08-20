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
        s.reverse()
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

def go_url(ll, url, pnt, history):
    if pnt is None and url == "google.com":
        ll.head = Node(url)
        ll.tail = ll.head
    elif pnt != None and pnt.data == url:
        pnt.next = Node(url)
        ll.tail = pnt.next
        return ll.tail
    elif pnt != None and pnt.next:
        pnt.next = Node(url)
        ll.tail = pnt.next
    else:
        ll.append(url)
    pnt = ll.tail
    history.append(url)
    return pnt

def backward(ll, pnt, history):
    if pnt is ll.head:
        return
    cur = ll.head
    while not ll.isEmpty() and cur.next:
        if cur.next is pnt:
            pnt = cur
            history.append(pnt.data)
            return pnt
        cur = cur.next
    return 

def forward(ll, pnt, history):
    if pnt is None:
        pnt = ll.head
        history.append(pnt.data)
    elif pnt.next:
        pnt = pnt.next
        history.append(pnt.data)
    return pnt

def backpath(ll, pnt):
    if pnt == None:
        return ""
    cur, s = ll.head, []
    while cur:
        s.append(str(cur.data))
        if cur == pnt:
            break
        cur = cur.next
    s.reverse()
    return " -> ".join(s)

ll = LinkedList()
pnt, history = ll.head, []
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[0] == 'E':
        pnt = go_url(ll, i[2:], pnt, history)
        #print(f"pnt : {pnt}")
    elif i[0] == 'B':
        pnt = backward(ll, pnt, history)
        #print(f"pnt : {pnt}")
    elif i[0] == 'F':
        pnt = forward(ll, pnt, history)
        #print(f"pnt : {pnt}")

print(f"History : {' -> '.join(history)}")
print(f"BackPath : {backpath(ll, pnt)}")