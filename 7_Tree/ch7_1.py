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
    
    def add(self, e):
        self.root = self.__addNode(e, self.root)
        return self.root
        
    def __addNode(self, e, r):
        # if self.root == None:
        #     self.root = Node(e)
        #     return r
        
        if r == None:
            r = Node(e)
        else:
            if e < r.data:
                r.left = self.__addNode(e, r.left)
            else:
                r.right = self.__addNode(e, r.right)
        
        return r
    
    def getMin(self, r: Node) -> Node:
        if r == None:
            return None
        
        if r.left == None:
            return r
        
        return self.getMin(r.left)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def remove(self, e):
        self.root = self.__removeNode(self.root, e) 
        return self.root
    
    def __removeNode(self, r: Node, e):
        if r == None:
            return r
        
        if e < r.data:
            r.left = self.__removeNode(r.left, e)
        elif e > r.data:
            r.right = self.__removeNode(r.right, e)
        else:
            if r.left == None or r.right == None:
                r = r.right if r.left == None else r.left
            else:
                m = self.getMin(r.right)
                print("Min of right =",m.data)
                r.data = m.data
                r.right = self.__removeNode(r.right, m.data)
        
        return r
    

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    # root = T.insert(i)
    root = T.add(i)
    
T.printTree(root)
print("-"*50)
root = T.remove(T.root.data)
T.printTree(root)
root = T.remove(T.root.data)
print("-"*50)
T.printTree(root)
