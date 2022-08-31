# '''Chapter : 5 - item : 2 - Doubly Linked List(append,insert,remove)'''


class Node:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data if data != None else None
        self.next = next if next != None else None
        self.prev = prev if prev != None else None


class LinkedList:
    def __init__(self) -> None:
        # dummy head & tail with a linear linked list
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail

    def __str__(self) -> str:
        s = []
        t = self.head.next
        while t != self.tail:
            s.append(t.data)
            t = t.next
        return '->'.join(s)

    def str_reverse(self) -> str:
        s = self.__str__().split('->')
        s = s[::-1]
        return '->'.join(s)

    def is_empty(self):
        return self.head.next == self.tail

    def append(self, data: str):
        current = self.head
        while current.next != self.tail:
            current = current.next

        apNode = Node(data, self.tail, current)
        current.next = self.tail.prev = apNode

    def insert(self, index: int, data: str):
        if index <= -1 or index > self.get_size():
            return False
        elif index == self.get_size():
            return self.append(data)

        current = self.head.next
        cur_i = 0

        while current.next != self.tail and cur_i != index:
            current = current.next
            cur_i += 1

        newNode = Node(data, current, current.prev)
        current.prev.next = current.prev = newNode

    def get_size(self):
        if self.is_empty():
            return 0

        t = self.head.next
        size = 1
        while t.next != self.tail:
            size += 1
            t = t.next

        return size

    def remove(self, data: str):
        # remove (pop)
        t = self.head
        t2 = t
        i = -1

        if not self.is_empty():
            while t.data != data and t.next != self.tail:
                t = t.next
                i += 1
            t2 = t
            t.prev.next = t.next
            t.next.prev = t.prev

        return t2, i if t2.data == data else 'Not Found!', '-1'


if __name__ == '__main__':
    inp = input('Enter Input : ').split(',')
    l = LinkedList()

    for j in inp:
        i = j.strip()
        # o = i.split()[0]
        if 'A' in i and 'Ab' not in i:
            l.append(i[2:])
        elif 'Ab' in i:
            l.insert(0, i[3:])
        elif 'I' in i:
            x = i.split()
            x = x[1].split(':')
            a = l.insert(int(x[0]), x[1])
            if a == False:
                print('Data cannot be added')
            else:
                print(f'index = {x[0]} and data = {x[1]}')
        elif 'R' in i:
            y = l.remove(i[2:])
            if y[1] == 'Not Found!':
                print(y[1])
            else:
                print(f'removed : {i[2:]} from index : {y[1]}')

        print(f'linked list : {l}')
        print(f'reverse : {l.str_reverse()}')
