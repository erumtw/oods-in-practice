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

    def insert(self, data, node=None):
        node = node if node != None else self.root

        # Code Here
        if self.root is None:
            self.root = Node(data)
            return

        if data >= node.data:
            if node.right is None:
                node.right = Node(data)
                return
            self.insert(data, node.right)
        else:
            if node.left is None:
                node.left = Node(data)
                return
            self.insert(data, node.left)

        return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def inorder(self, node, s=None):
        s = s if s != None else []
        if node:
            self.inorder(node.left, s)
            # print(node.data, "", end="")
            s.append(str(node.data))
            self.inorder(node.right, s)
            
        return " ".join(s)

    def preorder(self, node, s=None):
        s = s if s != None else []
        if node:
            s.append(str(node.data))
            self.preorder(node.left, s)
            self.preorder(node.right, s)
            
        return " ".join(s)

    def postorder(self, node, s=None):
        s = s if s != None else []
        if node:
            self.postorder(node.left, s)
            self.postorder(node.right, s)
            s.append(str(node.data))
            
        return " ".join(s)
    
    def breadth(self, node, s=None):
        s = s if s != None else []
        q = []
        q.append(node)
        while q != []:
            n = q.pop(0)
            s.append(str(n.data))
            if n.left != None:
                q.append(n.left)
            if n.right != None:
                q.append(n.right)
        
        return " ".join(s)
    
T = BST()
inp = [int(e) for e  in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
# T.printTree(root)

print("Preorder :", T.preorder(T.root))
print("Inorder :", T.inorder(T.root))
print("Postorder :", T.postorder(T.root))
print("Breadth :", T.breadth(T.root))
