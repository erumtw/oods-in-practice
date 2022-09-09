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

def getDigit(value, digit):
    # 0 -> หลักหน่วย
    value= int(value)
    for i in range(digit):
        value //= 10

    return  int(value) % 10
    
if __name__ == '__main__':
    
    inp = input("Enter Input : ").split()
    max_digit = [int(i) for i in inp]
    max_digit = max(max_digit)
    
    q = Queue(inp)
    qq = [
        Queue(), Queue(), Queue(), Queue(), Queue(), 
        Queue(), Queue(), Queue(), Queue(), Queue()
    ]
    
    # print(qq)
    for i in range(max_digit):
        while not q.isEmpty():
            cur_digit = getDigit(q.peek(), i)
            qq[cur_digit].nQ(q.dQ())

        for j in range(10):
            while not qq[j].isEmpty():
                q.nQ(qq[j].dQ())
    
    print(q.items)            

    # -123 456 -789 0 27 3645 133 -142 -5038594 15615 668 2 -1 72