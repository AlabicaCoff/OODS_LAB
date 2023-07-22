class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0
    
    def front(self):
        return self.queue[0]
    
    def rear(self):
        return self.queue[-1]

    def size(self):
        return len(self.queue)
    
def display(type):
    if type == "Enqueue" or type == "Dequeue":
        print(f"Step : {step}")
        print(f"{type} : {q.queue}")
        print(f"Error Dequeue : {err_dq}")
        print(f"Error input : {err_in}")
        print("--------------------")
    else:
        print(f"Step : {step}")
        print(q.queue)
        print(f"Error Dequeue : {err_dq}")
        print(f"Error input : {err_in}")
        print("--------------------")
    
inp = [data for data in input("input : ").split(",")]

q = Queue()
cnt, err_dq, err_in = 0, 0, 0

for step in inp:
    if step[0] == 'E':
        for i in range(int(step[1:])):
            q.enqueue(f"*{cnt}")
            cnt += 1
        display("Enqueue")
    elif step[0] == 'D':
        for i in range(int(step[1])):
            if q.is_empty():
                err_dq += 1
            else:
                q.dequeue()
        display("Dequeue")
    else:
        err_in += 1
        display("Error_Input")