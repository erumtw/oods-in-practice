class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Code Here
        if self.root is None:
            self.root = Node(data)    
            return self.root
        
        temp = self.root 
        while True:
            if data >= temp.data:
                if temp.right is None:
                    temp.right = Node(data)
                    break
                temp = temp.right
            else:
                if temp.left is None:
                    temp.left = Node(data)
                    break
                temp = temp.left
                
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def below(self, node, data, s=None):
        s = s if s != None else []
        if node is None:
            return 
        
        if node.left is not None:
            self.below(node.left, data, s)
            
        if node.data < data:
            s.append(node.data)
            
        if node.right is not None:
            self.below(node.right, data, s) 
    
        return s
            
        
            
inp = input("Enter Input : ").split('|') 
data = [int(e) for e in inp[0].split()]
d2 = int(inp[1])

T = BST()
for i in data:
    root = T.insert(i)
T.printTree(root)

print('--------------------------------------------------')
s = T.below(T.root, d2)
if s == []:
    print(f"Below {d2} : Not have")
else:
    s = [str(e) for e in s]
    print(f"Below {d2} : {' '.join(s)}")