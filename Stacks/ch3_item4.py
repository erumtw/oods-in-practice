# จงเขียนโปรแกรมเปลี่ยน Infix เป็น Postfix expression

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


def infix2postfix(exp):
    s = Stack()
    op = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []

    for c in exp:
        if c not in '+-*/^()':
            output.append(c)
        elif c in '()':
            if c == '(':
                s.push(c)
            else:
                while s.peek() != '(':
                    output.append(s.pop()) if s.peek() not in '()' else s.pop()
                s.pop()
        else:
            if s.is_empty():
                s.push(c)
            elif s.peek() in '()' or op[c] > op[s.peek()]:
                s.push(c)
            elif op[c] <= op[s.peek()]:
                for i in range(s.size()):
                    if s.peek() == '(':
                        break
                    if c in '*/' and s.peek() in '+-':
                        break
                    output.append(s.pop())
                s.push(c)

    if not s.is_empty():
        for i in range(s.size()):
            output.append(s.pop())

    return ''.join(output)


if __name__ == '__main__':

    print(" ***Infix to Postfix***")

    token = input("Enter Infix expression : ")

    print("PostFix : ")

    print(infix2postfix(token))
