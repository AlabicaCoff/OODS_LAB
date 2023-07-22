class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0
    
    def front(self):
        if self.is_empty():
            return None
        return self.items[0]
    
    def rear(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

inp = input("Enter width, height, and room: ").split(" ")

if inp == "":
    print("Invalid map input.")
    exit(0)

q = Queue()
w = int(inp[0])
h = int(inp[1])
room = inp[2].split(",")
deq_li = []

if len(room) != h:
    print("Invalid map input.")
    exit(0)
else:
    for row in room:
        if len(row) != w:
            print("Invalid map input.")
            exit(0)
        else:
            if 'F' in row:
                cur_pos = (row.index('F'), room.index(row))
                q.enqueue(cur_pos)
                deq_li.append(cur_pos)
    if not q.is_empty():
        print(f"Queue: {q.items}")
    else:
        print("Invalid map input.")
        exit(0)

while not q.is_empty():
    x, y = q.dequeue()
    if len(room) - 1 >= y - 1 and y - 1 >= 0:
        if room[y - 1][x] == '_' and (x, y - 1) not in deq_li and (x, y - 1) not in q.items:
            q.enqueue((x, y - 1))
        elif room[y - 1][x] == 'O':
            print("Found the exit portal.")
            exit(0)
        
    if len(room[y]) - 1 >= x + 1 and x + 1 >= 0:
        if room[y][x + 1] == '_' and (x + 1, y) not in deq_li and (x + 1, y) not in q.items:
            q.enqueue((x + 1, y)) #
        elif room[y][x + 1] == 'O':
            print("Found the exit portal.")
            exit(0)
        
    if len(room) - 1 >= y + 1 and y + 1 >= 0:
        if room[y + 1][x] == '_' and (x, y + 1) not in deq_li and (x, y + 1) not in q.items:
            q.enqueue((x, y + 1))
        elif room[y + 1][x] == 'O':
            print("Found the exit portal.")
            exit(0)
        
    if len(room[y]) - 1 >= x - 1 and x - 1 >= 0:
        if room[y][x - 1] == '_' and (x - 1, y) not in deq_li and (x - 1, y) not in q.items:
            q.enqueue((x - 1, y))
        elif room[y][x - 1] == 'O':
            print("Found the exit portal.")
            exit(0)

    deq_li.append((x, y))
    if not q.is_empty():
        print(f"Queue: {q.items}")
    
print("Cannot reach the exit portal.")