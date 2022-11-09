# Preorder , Inorder , Postorder และ Breadth First Search

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
        def insertion(data, r): # dont have to param self
            if r is None:
                r = Node(data)
            else:
                if data < r.data :
                    r.left = insertion(data, r.left)
                else:
                    r.right = insertion(data, r.right)
            return r
        
        self.root = insertion(data, self.root)
        return self.root

    def delete(self, data):
        def deletion(data, r: Node):
            if r == None:
                return r
            
            if data < r.data:
                r.left = deletion(data, r.left)
            elif data > r.data:
                r.right = deletion(data, r.right)
            else:
                # is leaf
                if r.right is None or r.left is None: # is leaf
                    r = r.right if r.right != None else r.left
                else: # isn't leaf
                    # find min of r.right node
                    minNode = self.getMin(r.right)
                    # swap delete Node with right min node
                    r.data = minNode.data
                    # delete minNode
                    r.right = deletion(minNode.data, r.right)
                
            return r     
                    
        self.root = deletion(data, self.root)
    
    def getMin(self, r=None):
        r = self.root if r == None else r
        if r == None:
            return None
        
        if r.left == None:
            return r
        
        return self.getMin(r.left)
        
    def getMax(self, r=None):
        r = self.root if r == None else r
        if r == None:
            return None
        
        if r.right == None:
            return r
        
        return self.getMin(r.right)
    
    def lessThanEqual(self, data):
        s = []
        def isbelow(data, node):
            if node is None:
                return 
            else:
                isbelow(data, node.left)
                isbelow(data, node.right)
                
                if node.data <= data:
                    s.append(node.data)
                    
        isbelow(data, self.root)
        return s
    
    def inOrder(self):
        s = []
        
        def travel(r):
            if r is None:
                return
            
            travel(r.left)
            s.append(str(r.data))
            travel(r.right)
            
        travel(self.root)
        return s
    
    def preOrder(self):
        s = []
        def travel(r):
            if r is None:
                return
            s.append(str(r.data))
            travel(r.left)
            travel(r.right)
            
        travel(self.root)
        return s

    def postOrder(self):
        s = []
        def travel(r):
            if r is None:
                return
            travel(r.left)
            travel(r.right)
            s.append(str(r.data))
            
        travel(self.root)
        return s

    def breadth(self): 
        q , s = [], []
        q.append(self.root)
        while( q != []):
            n = q.pop(0)
            s.append(str(n.data))
            if n.left != None:
                q.append(n.left)
            if n.right != None:
                q.append(n.right)
        return s
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]

for i in inp:
    root = T.insert(i)

# T.printTree(root)

# print(f"Preorder : {' '.join(T.preOrder())}")
print(f"Inorder : {' '.join(T.inOrder())}")
# print(f"Postorder : {' '.join(T.postOrder())}")
# print(f"Breadth : {' '.join(T.breadth())}")
T.delete(1)
print("---------")
# T.printTree(root)
print(f"Inorder : {' '.join(T.inOrder())}")
T.delete(10)
print(f"Inorder : {' '.join(T.inOrder())}")
T.delete(5)
print(f"Inorder : {' '.join(T.inOrder())}")
T.delete(4)
print(f"Inorder : {' '.join(T.inOrder())}")
T.delete(20)
print(f"Inorder : {' '.join(T.inOrder())}")
