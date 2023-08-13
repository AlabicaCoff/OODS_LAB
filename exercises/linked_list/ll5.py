class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    
class LinkedList:
    def __init__(self, head = None):
        if head is None:
            self.head = None
        else:
            self.head = head

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, []
        while cur:
            s.append(str(cur.data))
            cur = cur.next
        return " ".join(s)

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

    def bottom_up(self, pos, size):
        if 0 >= pos >= size or self.isEmpty():
            return
        else:
            lift_tail = self.search(pos - 1)
            tail = self.tail()
            tail.next = self.head
            tail = lift_tail
            self.head = lift_tail.next
            tail.next = None
    
    def riffle(self, pos):
        if self.isEmpty():
            return
        else:
            lift_head = self.head
            lift_tail = self.search(pos - 1)
            ll2 = LinkedList(lift_tail.next)
            lift_tail.next = None
            ll1 = LinkedList(lift_head)
            self.head = None

            cur1 = ll1.head
            cur2 = ll2.head

            while cur1 and cur2:
                self.append(cur1.data)
                self.append(cur2.data)
                cur1 = cur1.next
                cur2 = cur2.next

            while cur1:
                self.append(cur1.data)
                cur1 = cur1.next

            while cur2:
                self.append(cur2.data)
                cur2 = cur2.next

    def deriffle(self, pos, size):
        if self.isEmpty():
            return None
        else:
            if pos < size / 2:
                pull_out = pos - 1
            elif pos >= size / 2:
                pull_out = size - pos

            ll = LinkedList()
            cur = self.head
            while cur:
                if cur.next and ll.size() < pull_out:
                    ll.append(cur.next)
                    cur.next = cur.next.next
                cur = cur.next
            
            if ll.isEmpty():
                return
            ll.tail().next = None

            if pos < size / 2:
                riff_tail = self.search(pos - 1)
                ll.tail().next = riff_tail.next
                riff_tail.next = ll.head
            elif pos >= size / 2:
                self.tail().next = ll.head
            
def createLL(LL):
    linked_list = LinkedList()
    for item in LL:
        linked_list.append(item)
    return linked_list

def printLL(head):
    return head

def SIZE(head):
    return head.size()

def scarmble(head, b, r, size):
    pos1, pos2 = int(b / 100 * size), int(r / 100 * size)
    head.bottom_up(pos1, size)
    print(f"BottomUp {b:.3f} % : {head}")
    head.riffle(pos2)
    print(f"Riffle {r:.3f} % : {head}")
    head.deriffle(pos2, size)
    print(f"Deriffle {r:.3f} % : {head}")
    head.bottom_up(size - pos1, size)
    print(f"Debottomup {b:.3f} % : {head}")

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
for i in inp2.split('|'):
    h = createLL(inp1.split())
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)