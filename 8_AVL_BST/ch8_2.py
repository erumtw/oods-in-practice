class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left if left != None else None
        self.right = right if right != None else None
        self.height = self.setHeight()
            
    def setHeight(self):
        self.height = 1 + max(self.getHeight(self.left), self.getHeight(self.right))
        return self.height
    
    def getHeight(self, n):
        return n.height if n != None else -1
    
    def balanceFactor(self):
        # left - right of subtree
        # + ltilt Left, - tilt Right, 0 not tilt
        # 0 -
        # 1 / 2 //
        # -1 \ -2 \\
        return self.getHeight(self.left) - self.getHeight(self.right)
    
class AVLTree:
    def __init__(self) -> None:
        self.root = None
    
    def rotateLeft(self, r: Node):
        if r is None:
            return r
        
        newR = r.left
        r.left = newR.right
        newR.right = r
        r = newR
        r.right.setHeight()
        r.setHeight()
        return r

    def rotateRight(self, r: Node):
        if r is None:
            return r
        newR = r.right
        r.right = newR.left
        newR.left = r
        r = newR
        r.left.setHeight()
        r.setHeight()
        
        return r
    
    def insert(self, data):
        def insertion(data, r: Node):
            if r == None:
                print(f'Insert : ( {data} )')
                r = Node(data) 
            else:
                if data < r.data:
                    # print('L', end='')
                    r.left = insertion(data, r.left)
                else:
                    # print('R', end='')
                    r.right = insertion(data, r.right)
            # rebalance before return
            r = self.reBalance(r)
            return r

        self.root = insertion(data, self.root)
        # self.root = self.reBalance(self.root)
        return self.root
    
    def delete(self, data):
        def deletion(data, r:Node):
            if r is None:
                return r
            else:
                if data < r.data:
                    r.left = deletion(data, r.left)
                elif data < r.data:
                    r.right = deletion(data, r.right)
                else:
                    if r.right == None or r.left == None:
                        r = r.right if r.right != None else r.left
                    else:
                        minNode = self.getMin(r.right)
                        r.data = minNode.data
                        r.right = deletion(minNode.data, r.right)
            # rebalance before return
            r = self.reBalance(r)
            return r
        
        self.root = deletion(data, self.root)
        # self.root = self.reBalance(self.root)
        
    def preOrder(self, r: Node):
        s = []
        s.append(str(r.data))
        self.preOrder(r.left)
        self.preOrder(r.right)
        return " ".join(s)
    
    def getMin(self, r):
        if r == None:
            return None
        
        if r.left == None:
            return r
        
        return self.getMin(r.left)
    
    def reBalance(self, r: Node):
        if r == None:
            return r
        
        balance = r.balanceFactor()
        if balance == 2: # //
            if r.left.balanceFactor() == -1: # \
                r.left = self.rotateRight(r.left)
            r = self.rotateLeft(r)
        elif balance == -2: # \\
            if r.right.balanceFactor() == 1: # /
                r.right = self.rotateLeft(r.right)
            r = self.rotateRight(r)
            
        r.setHeight()
        return r
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)

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
    
if __name__ == "__main__":
    inp = input("Enter Input : ").split()
    T = AVLTree()
    
    for e in inp:
        T.insert(int(e))
        T.printTree(T.root)
        print("--------------------------------------------------")

    # print(T.preOrder())