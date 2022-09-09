class Stack:
    def __init__(self, items=None):
      self.items = items if items != None else []
    
    def push(self, element):
        self.items.append(element)
    
    def pop(self):
        if not self.isEmpty() :
            return self.items.pop() 
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1] 
        
    def isEmpty(self):
        return len(self.items) == 0
    
def evaluate(expreesion):
    stack = Stack()
    
    for e in expreesion:
        if e.isdigit():
           stack.push(e)
        else:
            if not stack.isEmpty():
                b = int(stack.pop())
                a = int(stack.pop())
                if e == '+':
                    stack.push(str(a + b))
                elif e == '-':
                    stack.push(str(a - b))
                elif e == '*':
                    stack.push(str(a * b))
                elif e == '/':
                    stack.push(str(a / b))
                    
    return stack
            
    
if __name__ == '__main__':
    inp = input("Enter expreesion : ")
    result = evaluate(inp)
    print(''.join(result.items))