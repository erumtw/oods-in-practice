'''
Parenthesis Matching
จงเขียนโปรแกรมเพื่อตรวจสอบว่า นิพจน์มีวงเล็บครบถ้วนหรือไม่ โดยใช้ Stack ช่วยในการแก้ปัญหา
โดยสามารถแจ้งได้ว่าข้อผิดพลาดที่เกิดขึ้นเกิดจากสาเหตุใด

1. มีวงเปิดไม่ตรงชนิดกับวงเล็บปิด
2. วงเล็บปิดเกิน
3. วงเล็บเปิดเกิน

แล้วให้แสดงผลตามตัวอย่าง
'''


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


def parenthesis_matching(items):
    open_stack = Stack()
    error_case = 0

    for e in items:
        if error_case == 0:
            if e in '[{(':
                open_stack.push(e)
            elif e in ']})':
                if open_stack.size() <= 0:  # close excess
                    error_case = 2
                elif not is_mathch(open_stack.pop(), e):
                    error_case = 1
        else:
            break

    if error_case == 0 and open_stack.size() > 0:  # open excess
        error_case = 3

    return error_case, open_stack


def is_mathch(opens, close): 
    return opens + close == '()' or \
        opens + close == '[]' or \
        opens + close == '{}'


if __name__ == '__main__':
    exps = input('Enter expresion : ')
    error_case, temp_stack = parenthesis_matching(exps)
    if error_case == 1:
        print(exps, 'Unmatch open-close')
    elif error_case == 2:
        print(exps, 'close paren excess')
    elif error_case == 3:
        print(exps, 'open paren excess  ', temp_stack.size(),
              ':', "".join(temp_stack.items))
    else:
        print(exps, 'MATCH')
