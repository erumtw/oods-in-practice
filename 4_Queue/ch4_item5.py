# Chapter4_item5 : Color Crush 2

class Stack:
    def __init__(self,  items=None):
        self.items = [] if items == None else items

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


def color_crush(colors: Stack, m_item: Queue, crush=None, is_normal=False, fail=0):
    items = Queue() if m_item.is_empty() else m_item
    crush = 0 if crush == None else crush
    temp_s = Stack()
    c = 0
    while not colors.is_empty():
        temp_s.push(colors.pop())
        # print(''.join(temp_s.items))
        if (not temp_s.is_empty()) and (not colors.is_empty()):
            if temp_s.peek() == colors.peek():
                c += 1
                if c == 2:
                    if is_normal and not items.is_empty():
                        temp_s.push(items.deQueue())
                        if temp_s.peek() == colors.peek():
                            fail += 1
                            c = 1
                        else:
                            c = 0
                    else:
                        for i in range(2):
                            temp_s.pop()
                        items.enQueue(
                            colors.pop()) if not is_normal else colors.pop()
                        c = 0
                        crush += 1
            else:
                c = 0

    if temp_s.size() >= 3:
        for j in range(temp_s.size()-1, 0, -1):
            if temp_s.items[j-2:j+1] == list(temp_s.items[j]*3):
                return color_crush(Stack(list(''.join(temp_s.items)[::-1])), items, crush, is_normal, fail)

    return temp_s, items, crush - fail, fail


if __name__ == '__main__':
    inp = input("Enter Input (Normal, Mirror) : ").split()
    colors_n = list(inp[0][::-1])
    colors_m = list(inp[1])

    mirror, m_items, m_crush, temp_fail = color_crush(Stack(colors_m), Queue())
    temp_fail = None

    if mirror.items == []:
        mirror.items = list('Empty')

    normal, temp2, n_crush, fail = color_crush(
        Stack(colors_n), m_items, is_normal=True)
    temp2 = None

    if normal.items == []:
        normal.items = list('ytpmE')

    print('NORMAL :')
    print(normal.size()) if normal.items != list('ytpmE') else print(0)
    print(''.join(normal.items[::-1]), '\n',
          f'{n_crush} Explosive(s) ! ! ! (NORMAL)', sep='')
    if fail >= 1:
        print(f'Failed Interrupted {fail} Bomb(s)')
    print('------------MIRROR------------')
    print(': RORRIM')
    print(mirror.size()) if mirror.items != list('Empty') else print(0)
    print(''.join(mirror.items[::-1]), '\n',
          f'(RORRIM) ! ! ! (s)evisolpxE {m_crush}', sep='')