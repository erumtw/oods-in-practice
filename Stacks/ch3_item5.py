'''ที่จอดรถของนาย ก เป็นส่วนที่แรเงาสีฟ้า ส่วนสีแดงเป็นที่ของนาย ข ซี่งเป็นญาติกัน ที่จอดรถของนาย ก และ นาย ข แคบมาก จอดรถได้เรียงเดี่ยว นาย ข ไม่ได้ใช้ที่จอดรถ แต่ อนุญาติให้นาย ก ใช้ที่จอดรถของเขาได้โดยไม่จอดรถแช่ไว้ เนื่องจากซอยแคบ ดังนั้นการมาจอด (arrive) และการรับรถ (depart)จะเป็นลักษณะของ stack เงื่อนไขคือ ในการรับรถ x ใดๆอยากให้ลำดับรถเป็นเหมือนเดิม ดังรูป simulate การจอดรถในที่จอดรถของนาย ก โดยใช้ operation ของ stack ข้างล่างเป็นตัวอย่าง output

การรับ input : รับ input 4 ค่าใน 1 บรรทัดโดยให้แยกโดย " " (space bar) โดยตำแหน่งแรกคือ จำนวนสูงสุดที่รถสามารถจอดได้ในซอยของ นาย ก ตำแหน่งที่สองคือ รถที่จอดอยู่ในซอยของ นาย ก ตำแหน่งที่สามคือ การกระทำเช่น ถ้าเป็น arrive จะทำการเพิ่มรถในซอย ส่วน depart จะทำการเอารถออกจากซอย โดยรถที่จะทำการเพิ่มหรือนำออกนั้นจะเป็น เลขในตำแหน่งที่ 4

***หมายเหตุ ถ้าในซอยไม่มีรถอยู่เลยให้ input = 0 ในตำแหน่งที่ 2***

*** สามารถสร้างได้มากกว่า 1 stack ***'''


class Stack:

    def __init__(self,  items=None):
        if items == None:
            self.items = []
        else:
            self.items = items

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def depart(s, n):
    a = Stack(s)
    b = Stack()

    while a.peek() != n:
        b.push(a.pop())

    if a.peek() == n:
        a.pop()
        for i in range(b.size()):
            a.push(b.pop())

    return a.items


if __name__ == '__main__':

    print("******** Parking Lot ********")
    m, s, o, n = input("Enter max of car,car in soi,operation : ").split()
    m, n = int(m), int(n)
    s = [int(c) for c in s.split(',')] if s != '0' else []

    if len(s) == m and o == 'arrive' and n not in s:
        print(f'car {n} cannot arrive : Soi Full')
        print(s)
    elif o == 'arrive' and n in s:
        print(f'car {n} already in soi')
        print(s)
    elif o == 'depart' and s == []:
        print(f'car {n} cannot depart : Soi Empty')
        print(s)
    elif o == 'depart' and n not in s:
        print(f'car {n} cannot depart : Dont Have Car {n}')
        print(s)
    else:
        if o == 'arrive':
            s.append(n)
            print(f'car {n} arrive! : Add Car {n}', '\n', s, sep='', end='')
        else:
            print(f'car {n} depart ! : Car {n} was remove',
                  '\n', depart(s, n), sep='', end='')
            