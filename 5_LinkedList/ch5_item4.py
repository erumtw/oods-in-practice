# Chapter : 5 - item : 4 - หา loop ใน linked list

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
        if self.is_empty():
            return 'Empty'

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
        rear = self.tail.prev
        rear.next = Node(data, self.tail, rear)
        self.tail.prev = rear.next

        # current = self.head
        # while current.next != self.tail:
        #     current = current.next

        # apNode = Node(data, self.tail, current)
        # current.next = self.tail.prev = apNode

    # this insert only for ch5-4
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

        newNode = Node(data, self.tail, current.prev)
        current.prev.next = self.tail.prev = newNode

    def getData(self, index):
        if self.is_empty() or index >= self.get_size():
            return -1
        else:
            t = self.head.next
            cur_i = 0
            while t.next != self.tail and cur_i != index:
                cur_i += 1
                t = t.next
            return t.data

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

    def set_next(self, index1, index2): # set เสร็จตัดหลังทิ้งหมด เอาเทลมาต่อเลย
        error = 0
        loop = False

        if self.is_empty():  # -> Error! {list is empty} -> error = 1
            error = 1
        elif index1 >= self.get_size():
            # index1 out of range : -> Error! {index not in length}: index1 -> error = 2
            error = 2
        elif index2 >= self.get_size():
            # index2 out of range, then append index2 as value -> error = 3
            error = 3
            self.append(str(index2))
        else:  # set node.next
            # Set node.next complete!, index:value = i1:value of i1 -> i2:value of i2
            self.insert(int(index1)+1, self.getData(int(index2)))

        if index2 <= index1 and error == 0:
            loop = True

        return error, loop


if __name__ == '__main__':
    inp = input('Enter input : ').split(',')
    L = LinkedList()
    loop = False

    for i in inp:
        i = i.strip().split()
        if 'A' in i:
            L.append(i[1].strip())
            print(f'{L}')
        elif 'S' in i:
            n = i[1].split(':')
            a, b = L.getData(int(n[0])), L.getData(int(n[1]))
            error, loop = L.set_next(int(n[0]), int(n[1]))
            if error == 0:
                print(
                    f'Set node.next complete!, index:value = {n[0]}:{a} -> {n[1]}:{b}')
                # print(L)
            elif error == 1:
                print("Error! {list is empty}")
            elif error == 2:
                print("Error! {index not in length}:", n[0])
            else:
                print(f'index not in length, append : {n[1]}')
                # print(f'{L}')

    print('Found Loop') if loop == True else print(f'No Loop\n{L}')