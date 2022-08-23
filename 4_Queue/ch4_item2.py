'''จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue
โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้
แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ
แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ
ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2
จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2]
'''

class Queue:

    def __init__(self, items=None):
        self.items = [] if items == None else items

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    items = input('Enter people and time : ').split()
    q = Queue(list(items[0]))
    cashier1, cashier2 = Queue(), Queue()
    t1, t2 = 0, 0

    for i in range(int(items[1])):
        if not q.is_empty():
            if cashier1.size() < 5:
                cashier1.enQueue(q.deQueue())
            else:
                if cashier2.size() < 5:
                    cashier2.enQueue(q.deQueue())
        
        print(f'{i+1} {q.items} {cashier1.items} {cashier2.items}')
        
        if not cashier1.is_empty():
            t1 += 1
            if t1 % 3 == 0:
                cashier1.deQueue()
                t1 = 0
        
        if not cashier2.is_empty():
            t2 += 1
            if t2 % 2 == 0:
                cashier2.deQueue()
                t2 = 0