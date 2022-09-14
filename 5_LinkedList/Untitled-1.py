class LLQueue:

    class Node:
        def __init__(self, data=None, next=None, prev=None) -> None:
            self.data = data if data != None else None
            self.next = next if next != None else None
            self.prev = prev if prev != None else None

    def __init__(self, items=None) -> None:
        # dummy nodes
        self.head = self.Node()
        self.tail = self.Node(prev=self.head)
        self.head.next = self.tail

        if items != None:
            for e in items:
                self.enQueue(e)

    def enQueue(self, data):
        # append ต่อท้าย
        rear = self.tail.prev
        rear.next = self.Node(data, self.tail, rear)
        self.tail.prev = rear.next

    def deQueue(self):
        if self.isEmpty():
            return print("Queue is Empty")
        else:
            dq = self.head.next
            self.head.next = dq.next
            return dq.data

    def isEmpty(self):
        return self.head.next == self.tail

    def peek(self):
        return self.head.next.data

    def __len__(self):
        if self.isEmpty():
            return 0
        else:
            t = self.head.next
            size = 0
            while t.next != self.tail:
                size += 1
            return size

    def __str__(self) -> str:
        if self.isEmpty():
            return ''
        else:
            t = self.head.next
            s = []
            while t != self.tail:
                s.append(str(t.data))
                t = t.next
            return ' '.join(s)
        
data = [10, 10,10,10,10,10,10,10,10,10,10,10,10,10,10]        
q = LLQueue(data)
qq = LLQueue()
print(f"q = {q}")
print(f"qq = {qq}")

while not q.isEmpty():
    qq.enQueue(q.deQueue())
    
print(f"q = {q}")
print(f"qq = {qq}")

while not qq.isEmpty():
    q.enQueue(qq.deQueue())
print(f"qq = {qq}")
print(f"q = {q}")