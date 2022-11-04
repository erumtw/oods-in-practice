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


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)