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
            