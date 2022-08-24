'''
หลังจากกฤษฎาล้างจานเสร็จ ก็ได้มาเล่นเกมส์ที่กำลังเป็นที่นิยมทั่วโลกในตอนนี้   Microsoft Flight Simulator ?  Fall Guys ?  Valorant ?  "ผิดทั้งหมด!"
กฤษฎาได้กล่าวไว้  เกมที่กำลังเป็นที่นิยมคือ Color Crush ต่างหาก   โดยเกมนี้จะเป็นการนำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน
เช่น  A B B B A  -> A A เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  โดยถ้าหากมีการระเบิดตั้งแต่ 2 ครั้งขึ้นไปจะแสดง Combo ขึ้นมา
โดยเมื่อการระเบิดสิ้นสุดลงให้แสดงจำนวนและลำดับของสีที่เหลือจากขวาไปซ้าย'''


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
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def color_crush(s: Stack, lst, crush=None):
    if crush == None:
        crush = 0

    if len(lst) < 3:
        s.items = lst
        return s, crush

    i = len(lst)-1

    while i >= 2:
        if lst[i-2:i+1] == list(lst[i]*3):
            crush += 1
            i = i-3 if i > 2 else i-2
        else:
            s.push(lst[i])
            i -= 1

    if i >= 0 and not s.is_empty():
        for i in range(i, 0, -1):
            s.push(lst[i])
        s.push(lst[0])

        if s.size() >= 3:
            for j in range(s.size()-1, 0, -1):
                if s.items[j-2:j+1] == list(s.items[j]*3):
                    return color_crush(Stack(), list(''.join(s.items)[::-1]), crush)

    return s, crush


def color_crush2(colors: Stack):
    temp_s = Stack()
    c = 0

    while not colors.is_empty():
        temp_s.push(colors.pop())
        if (not temp_s.is_empty()) and (not colors.is_empty()):
            if temp_s.peek() == colors.peek():
                c += 1
                if c == 2:
                    for i in range(2):
                        temp_s.pop()
                    colors.pop()
                    c = 0
            else:
                c = 0

    print(''.join(temp_s.items))

    if temp_s.size() >= 3:
        for j in range(temp_s.size()-1, 0, -1):
            if temp_s.items[j-2:j+1] == list(temp_s.items[j]*3):
                return color_crush(Stack(list(''.join(temp_s.items)[::-1])))

    return ''.join(temp_s.items)


inp = input('Enter Input : ').split()
S = Stack()

S, crush = color_crush(S, inp)
print(S.size())
print("".join(S.items)) if not S.is_empty() else print("Empty")

if crush > 1:
    print(f'Combo : {crush} ! ! !')
