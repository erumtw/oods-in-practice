class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None if next == None else next

class LinkedList:
    def __init__(self, head=None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            # head
            self.head = head
            self.size = 1
            
            t = self.head
            # tail
            while t.next != None:
                t = t.next
                self.size += 1
            self.tail = t
            
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head == None:
            self.head = self.tail = Node(item)
        else:
            p = Node(item)
            self.tail.next = p
            self.tail = p 
        self.size += 1
        
    def addHead(self, item):
        if self.head == self.tail == None:
            self.head = self.tail = Node(item)
        else:
            self.head = Node(item, self.head)
        self.size += 1
            
    def search(self, item):
        if self.head == self.tail == None:
            return 'Not Found'
        else:
            finder = self.head
            while finder.value != item and finder.next != None:
                finder = finder.next
            return 'Found' if finder.value == item else 'Not Found'
            

    def index(self, item):
        if self.head == None:
            return -1
        else:
            index = 0
            finder = self.head
            while finder.value != item and finder.next != None:
                finder = finder.next
                index += 1
            return index if str(finder.value) == str(item) else -1

    def get_size(self):
        return self.size

    def pop(self, pos):
        if self.head == None or 0 < pos >= self.size:
            return 'Out of Range'
        elif pos == 0:
            self.head = self.head.next
            self.size -= 1
        elif pos == self.size-1:
            prevTail = self.head
            while prevTail.next.next != None:
                prevTail = prevTail.next
            prevTail.next = prevTail.next.next
            self.size -= 1
        else:
            finder = self.head
            index = 0
            prev_finder = finder
            while index != pos and finder.next != None:
                index += 1
                prev_finder = finder
                finder = finder.next
            prev_finder.next = finder.next
            self.size -= 1
        return 'Success'
            
            
        
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.get_size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)