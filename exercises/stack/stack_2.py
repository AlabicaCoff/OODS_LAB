# Chapter : 3 - item : 2 - แ ต ก ดั ง เ พ ล้ ง ! ! !
# กฤษฎาได้ถูกคุณแม่ไหว้วานให้ล้างจานกองเป็นภูเขา  แต่ทว่ากฤษฎาก็ได้สังเกตเห็นว่าจานแต่ละใบนั้นมีน้ำหนักที่แตกต่างกัน และบนจานยังมีตัวเลขอีกด้วย  กฤษฎาได้เหม่อลอยเนื่องจากครุ่นคริสว่าตัวเลขนั้นหมายถึงอะไร  กฤษฎาก็ได้ทำจานหลุดมือจนจานแตก  และเมื่อจานแตกได้มีเสียงที่มีความถี่ตามเลขบนจาน  กฤษฎาจึงนึกสนุกได้นำจานขนาดต่างๆและมีความถี่ต่างกันมาวางซ้อนๆกัน  โดยถ้าหากนำจานที่มีน้ำหนักมากกว่ามาวางบนจานที่มีน้ำหนักน้อยกว่า จะทำให้จานที่มีน้ำหนักน้อยกว่า แตก !!! และจะแตกไปเรื่อยๆจนกว่าจานใบด้านล่างจะมีน้ำหนักเท่ากันหรือมากกว่า หรือจนกว่าจะไม่มีจานด้านล่างมารองรับแล้ว

# ให้น้องๆเขียนโปรแกรมอ่านลำดับของจานที่กฤษฎาได้วางลงไปโดยให้ใส่จานทีละใบ  ซึ่งรวมถึงขนาดของจานและความถี่ของจาน  จากนั้นให้หาว่าลำดับของความถี่ของจานที่ได้ยินเมื่อวางจานลงไปตามนั้นแล้วจะเป็นเช่นใด

# อธิบาย Input : จะมีแค่รูปแบบเดียวคือ   < a  b >  โดยที่  a = น้ำหนักของจาน  ,  b = ความถี่ของจาน

class Stack:
    def __init__(self):
        self.lst = []

    def size(self):
        return len(self.lst)
    
    def peek(self):
        return self.lst[-1]

    def is_empty(self):
        if len(self.lst) == 0:
            return True
        else:
            return False
    
    def pop(self):
        if not self.is_empty():
            return self.lst.pop()

    def push(self, item):
        self.lst.append(item)

plt_data = [inp.split(" ") for inp in input("Enter Input : ").split(",")]

s = Stack()

w, f = 0, 1 # w = weight, f = frequency

for plt in plt_data:
    if plt_data.index(plt) == 0: # Push first plate to stack
        s.push(plt)
        continue
    elif int(s.peek()[w]) >= int(plt[w]): # Push plate to stack if previous plate's weight >= plate's weight
        s.push(plt)
        continue
    while int(s.peek()[w]) < int(plt[w]): # Loop if previous plate's weight < plate's weight
        print(s.pop()[f]) # Pop previous plate out and print frequency
        if s.is_empty(): # Push plate's to stack if stack is empty
            s.push(plt)
        elif int(s.peek()[w]) >= int(plt[w]): # Push plate to stack if previous plate's weight >= plate's weight
            s.push(plt)
        elif s.size() < 1: # Break the loop if stack's size < 1
            break