# radix sort

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
            dq.next.prev = dq.prev
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
            return ' -> '.join(s)

    def str_reverse(self) -> str:
        s = self.__str__().split(' -> ')
        s = s[::-1]
        return ' -> '.join(s)

def get_digit(value, digit):
    # 0 -> หลักหน่วย
    for i in range(digit):
        value = int(value)
        value //= 10

    return str(int(value) % 10)

def splitPosNeg(arr):
    pos = []
    neg = []
    for e in arr:
        # e = int(e)
        if int(e) < 0:
            neg.append(e)
        else:
            pos.append(e)
    return pos, neg

def is_mixedsign(arr):
    pos = 0
    neg = 0
    for i in arr:
        # i = int(i)
        if int(i) < 0:
            neg += 1
        else:
            pos += 1
        if pos > 0 and neg > 0:
            return True
        
    return False

def getMaxDigit(arr):
    max = int(arr[0])
    for i in arr:
        i = int(i)
        if i < 0:
            i *= -1

        if i > max:
            max = i

    return str(max)

def radix_sort(arr, isDisplay=False):
    q = LLQueue(arr)
    
    max_digits = getMaxDigit(arr)
    
    qq = [
        LLQueue(), LLQueue(), LLQueue(), LLQueue(), LLQueue(),
        LLQueue(), LLQueue(), LLQueue(), LLQueue(), LLQueue()
    ]
    
    # print("------------------------------------------------------------")
    for i in range(len(str(max_digits))):
        
        while not q.isEmpty():
            if int(q.peek()) < 0:
                cur_digit = get_digit(str(q.peek()[1:]), i)
            else:
                cur_digit = get_digit(str(q.peek()), i)
            qq[int(cur_digit)].enQueue(str(q.deQueue()))
        # if isDisplay == True:
        #     print("Round : " + str(i))
        
        for j in range(10):
            # if isDisplay == True:
            #     print(f"{j} : {qq[j]}")
                
            while not qq[j].isEmpty():
                q.enQueue(str(qq[j].deQueue()))
                
        # if isDisplay == True:
        #     print("------------------------------------------------------------")
                

    return q


if __name__ == '__main__':
    inp = input('Enter input : ').split()
    
    print(f"{len(getMaxDigit(inp))} Time(s)")
    print("Before Radix Sort :", " -> ".join(inp))
    
    if is_mixedsign(inp):
        pos, neg = splitPosNeg(inp)
        qpos = radix_sort(pos)
        qneg = radix_sort(neg)
        
        # print(' '.join(qneg.items), ' '.join(qpos.items))
        radix_sort(inp, True)
        print("After  Radix Sort :", qneg.str_reverse()," ->", qpos)
    else:   
        print("After  Radix Sort :", radix_sort(inp))
    
    
    
            