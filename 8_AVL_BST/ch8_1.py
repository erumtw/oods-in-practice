class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left if left != None else None
        self.right = right if right != None else None
        
class AVLTree:
    def __init__(self) -> None:
        self.root = None
        
    def insert(self, data):
        def insertion(data, root: Node):
            if root == None:
                print('*')
                root = Node(data) 
            else:
                if data < root.data:
                    print('L', end='')
                    root.left = insertion(data, root.left)
                else:
                    print('R', end='')
                    root.right = insertion(data, root.right)
            return root

        self.root = insertion(data, self.root)
    
if __name__ == "__main__":
    inp = input("Enter Input : ").split()
    T = AVLTree()
    for e in inp:
        T.insert(int(e))