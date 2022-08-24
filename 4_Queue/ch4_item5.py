# Chapter4_item5 : Color Crush 2

'''
Enter Input (Normal, Mirror) : AAABBBCDEE HHH
NORMAL :
8
EEDCAHAA
1 Explosive(s) ! ! ! (NORMAL)
------------MIRROR------------
: RORRIM
0
ytpmE
(RORRIM) ! ! ! (s)evisolpxE 1
'''
class Stack:

    def __init__(self,  items=None):
        if items == None:
            self.items = []
        else:
            self.items = items

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
    
def color_crush(colors: Stack):
    temp_s = Stack()
    c = 0
    
    while not colors.is_empty():
        temp_s.push(colors.pop())
        if (not temp_s.is_empty()) and (not colors.is_empty()):
            if temp_s.peek() == colors.peek():
                c += 1
                if c == 2:
                    for i in range(2):
                        temp_s.pop()
                    colors.pop()
                    c = 0
            else:
                c = 0
                
    print(''.join(temp_s.items))

    if temp_s.size() >= 3:
            for j in range(temp_s.size()-1, 0, -1):
                if temp_s.items[j-2:j+1] == list(temp_s.items[j]*3):
                    return color_crush(Stack(list(''.join(temp_s.items)[::-1])))
    
    return ''.join(temp_s.items)
                
            
if __name__ == '__main__':
    inp = input("Enter Input (Normal, Mirror) : ").split()
    colors = list(inp)
    color_crush(Stack(colors))
    