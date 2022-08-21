'''ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ Queue ในการแก้ปัญหา

E  <value>  ให้นำ value ไปใส่ใน Queue และทำการแสดงผล ข้อมูลปัจจุบันของ Queue

D                 ให้ทำการ Dequeue ตัวที่อยู่หน้าสุดของ Queue ออก หลังจากนั้นแสดงตัวเลขที่เอาออกมา และ แสดงผลข้อมูล
                    ปัจจุบันของ Queue

***และเมื่อจบการทำงานให้แสดงผลข้อมูลปัจจุบันของ Queue พร้อมกับข้อมูลที่ถูก Dequeue ทั้งหมดตามลำดับ
***ถ้าหากไม่มีข้อมูลใน Queue แล้วให้แสดงคำว่า  Empty'''


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

    inp = input('Enter Input : ').split(',')
    q = Queue()
    temp = []

    for c in inp:
        if 'E' in c:
            q.enQueue(c[2])
            print(', '.join(q.items))
        elif c == 'D':
            if not q.is_empty(): 
                temp.append(q.deQueue())
                if q.size() < 1:
                    print(temp[-1], '<-', 'Empty')
                else:
                    print(temp[-1], '<-', ', '.join(q.items))
            else:
                print('Empty')
                pass

    if q.is_empty() and len(temp) == 0:
        print('Empty :', 'Empty')
    elif len(temp) == 0:
        temp = 'Empty'
        print('Empty :', ', '.join(q.items))
    else:
        print(''.join(temp), ':', end='') if len(
            temp) < 2 else print(', '.join(temp), ':', end='')
        print(' Empty') if q.is_empty() else print('', ', '.join(q.items))
