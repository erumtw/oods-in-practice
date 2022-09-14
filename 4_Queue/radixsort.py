class Queue:
    def __init__(self, items=None) -> None:
        self.items = items if items != None else []

    def isEmpty(self):
        return len(self.items) == 0

    def getSize(self):
        return len(self.items)

    def nQ(self, e):
        self.items.append(e)

    def dQ(self):
        return self.items.pop(0)

    def peek(self):
        if not self.isEmpty():
            return self.items[0]

    def __str__(self) -> str:

        # for i in range(self.getSize()):
        #     self.items[i] = str(self.items[i])

        return ' '.join(self.items)
    
def getDigit(value, digit):
    # 0 -> หลักหน่วย
    for i in range(digit):
        value = int(value)
        value //= 10

    return str(int(value) % 10)


def getMaxDigit(arr):
    max = int(arr[0])
    for i in arr:
        i = int(i)
        if i < 0:
            i *= -1

        if i > max:
            max = i

    return max


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

def radix_sort(arr):
    q = Queue(arr)
    
    max_digit = getMaxDigit(arr)
    
    qq = [
        Queue(), Queue(), Queue(), Queue(), Queue(),
        Queue(), Queue(), Queue(), Queue(), Queue()
    ]
    
    for i in range(len(str(max_digit))):
            
        while not q.isEmpty():
            if int(q.peek()) < 0:
                cur_digit = getDigit(str(q.peek())[1:], i)
            else:
                cur_digit = getDigit(str(q.peek()), i)
            qq[int(cur_digit)].nQ(q.dQ())

        for j in range(10):
            while not qq[j].isEmpty():
                q.nQ(qq[j].dQ())
                
    return q
                
if __name__ == '__main__':

    inp = input("Enter Input : ").split()
    if is_mixedsign(inp):
        pos, neg = splitPosNeg(inp)
        qpos = radix_sort(pos)
        qneg = radix_sort(neg)
        qneg.items = qneg.items[::-1]
        # print(' '.join(qneg.items), ' '.join(qpos.items))
        print(qneg, qpos)
    else:   
        print(' '.join(radix_sort(inp).items))

    # -123 456 -789 0 27 3645 133 -142 -5038594 15615 668 2 -1 72
