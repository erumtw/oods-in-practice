# ให้นักศึกษา สร้าง class Stack ด้วย list ของ python โดย มี method ดังต่อไปนี้

class Stack:
    
    def __init__(self,  items=None):
        if items == None:
            self.items = []
        else:
            self.items = items
         
    # เก็บข้อมูลลง stack   
    def push(self, i):        
        self.items.append(i)
        
    # นำข้อมูลออกจาก stack    
    def pop(self):          
        return self.items.pop()

    # ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false
    def isEmpty(self):    
        return len(self.items) == 0

    #    ตรวจสอบจำนวนข้อมูลใo stack
    def size(self):  
        return len(self.items)


# แล้วให้โปรแกรมรับข้อมูล เพื่อเก็บใน stack และให้ทำงานตาม code คำสั่งต่อไปนี้

print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():

    s.pop()

print(s.size(),"Data in stack : ",s.items)