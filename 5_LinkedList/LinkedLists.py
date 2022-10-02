class LinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data if data != None else None
            self.prev = prev if prev != None else None
            self.next = next if next != None else None

    def __init__(self, arr=None):
        # init dummy head/tail nodes
        self.head = self.Node()
        self.tail = self.Node(prev=self.head)

        self.head.next = self.tail

        if arr != None:
            for e in arr:
                self.append(e)

    def __str__(self):
        if self.is_empty():
            return "Empty"
        else:
            s = []
            t = self.head.next 
            while t != self.tail:
                s.append(t.data)
                t = t.next
                
            return "".join(s)

    def strReverse(self):
        s = self.__str__()
        s = s[::-1]
        return s
    
    def append(self, data):
        newNode = self.Node(data, self.tail.prev, self.tail)
        self.tail.prev.next = self.tail.prev = newNode

    def insert(self, index, data):
        if index > self.size() or index < 0:
            return print("Out Of Range")
        elif index == self.size():
            self.append(data)
        else:
            if index == self.size()-1:
                return self.append(data)
            
            i = 0
            t = self.head.next
            while i < index:
                i += 1
                t = t.next
            inNode = self.Node(data, t.prev, t)
            t.prev.next = t.prev = inNode
            
    def is_empty(self):
        return self.head.next == self.tail

    def size(self):
        if self.is_empty():
            return 0
        
        t = self.head.next
        size = 0
        while t != self.tail:
            size += 1 
            t = t.next
            
        return size
    
    def popleft(self):
        popNode = self.head.next
        
        self.head.next = popNode.next
        popNode.next.prev = self.head
        
        return popNode.data
    
    def popright(self):
        popNode = self.tail.prev
        
        self.tail.prev = popNode.prev
        popNode.prev.next = self.tail
        
        return popNode.data
            
if __name__ == '__main__':
    arr = ['a','b','c','d']
    LL = LinkedList(arr)
    print(LL)
    LL.append('e')
    LL.insert(6,'x')
    print(LL, LL.size())
    
    LL.popleft()
    print(LL, LL.size())
    LL.popright()
    print(LL, LL.size())