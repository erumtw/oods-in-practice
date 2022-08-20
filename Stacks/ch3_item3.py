# '''
# หลังจากกฤษฎาล้างจานเสร็จ ก็ได้มาเล่นเกมส์ที่กำลังเป็นที่นิยมทั่วโลกในตอนนี้   Microsoft Flight Simulator ?  Fall Guys ?  Valorant ?  "ผิดทั้งหมด!"
# กฤษฎาได้กล่าวไว้  เกมที่กำลังเป็นที่นิยมคือ Color Crush ต่างหาก   โดยเกมนี้จะเป็นการนำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน
# เช่น  A B B B A  -> A A เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  โดยถ้าหากมีการระเบิดตั้งแต่ 2 ครั้งขึ้นไปจะแสดง Combo ขึ้นมา

# โดยเมื่อการระเบิดสิ้นสุดลงให้แสดงจำนวนและลำดับของสีที่เหลือจากขวาไปซ้าย'''


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


def colorCrush(s: Stack, lst, crush=None):
    if crush == None:
        crush = 0

    if len(lst) < 3:
        s.items = lst
        return s, crush

    i = len(lst)-1

    while i >= 2:
        if lst[i-2:i+1] == list(lst[i]*3):
            crush += 1
            if i > 2:
                i -= 3
            else:
                i -= 2
        else:
            s.push(lst[i])
            i -= 1

    if i >= 0 and s.is_empty() == False:
        for i in range(i, 0, -1):
            s.push(lst[i])
        s.push(lst[0])

        if s.size() >= 3:
            for j in range(s.size()-1, 0, -1):
                if s.items[j-2:j+1] == list(s.items[j]*3):
                    return colorCrush(Stack(), list(''.join(s.items)[::-1]), crush)
    # else:
    #     s.push(lst[0])

    return s, crush


inp = input('Enter Input : ').split()
S = Stack()

S, crush = colorCrush(S, inp)
print(S.size())
print("".join(S.items)) if S.is_empty() == False else print("Empty")

if crush > 1:
    print(f'Combo : {crush} ! ! !')
