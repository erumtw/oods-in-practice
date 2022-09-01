# Chapter : 5 - item : 3 - รวม Linked List
# ให้น้องรับ Linked List มา 2 ตัว จากนั้นนำ 2 Linked List มาต่อกัน โดย L2 จะมาต่อ L1 แบบกลับหลัง

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

    def __str__(self):
        s = []
        t = self.head.next
        while t != self.tail:
            s.append(t.data)
            t = t.next
        return s

    def str_reverse(self):
        s = self.__str__()
        s = s[::-1]
        return s

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
    L1 = LinkedList()
    L2 = LinkedList()
    
    in1, in2 = input("Enter Input (L1,L2) : ").split()
    in1 = in1.split('->')
    in2 = in2.split('->')
    
    for e in in1:
        L1.append(e)
        
    for e in in2:
        L2.append(e)
        
    print(f'L1    : {" ".join(L1.__str__())}')
    print(f'L2    : {" ".join(L2.__str__())}')
    print(f'Merge : {" ".join(L1.__str__())} {" ".join(L2.str_reverse())}')