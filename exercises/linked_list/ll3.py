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
        return "->".join(s)

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
                
dict = {}
inp = input("Enter input: ")
n, datas = inp.split(' ')
for data in datas.split(','):
    b1, b2 = data.split('-')
    if b1 in dict.keys() and b2 in dict.keys():
        dict[b1].tail.next = dict[b2].head
        dict[b1].tail = dict[b2].tail
        b2_ll, cur = [], dict[b2].head
        while cur:
            b2_ll.append(cur.data)
            cur = cur.next
        for k in dict.keys():
            if k in b2_ll:
                dict[k] = dict[b1]
    elif b1 not in dict.keys() and b2 in dict.keys():
        if dict[b2].pop(b2) is dict[b2].head:
            dict[b2].add_head(b1)
            dict[b1] = dict[b2]
    else:
        if b1 not in dict.keys():
            dict[b1] = LinkedList(Node(b1))
        if b2 not in dict.keys():
            dict[b1].append(b2)
            cur = dict[b1].head
            dict[b2] = dict[b1]
        
for i in range(1, int(n) + 1):
    if str(i) not in dict.keys():
        dict[str(i)] = LinkedList(Node(str(i)))

ol, tmpl = [], []
for k in dict.keys():
    if dict[k].head.data not in ol:
        ol.append(dict[k].head.data)
        tmpl.append(dict[k])

cnt = 0
for num in sorted(list(map(int, ol))):
    for ll in tmpl:
        if int(ll.head.data) == num:
            cnt += 1
            print(f"{cnt}: {ll}")
print(f"Number of train(s): {cnt}")