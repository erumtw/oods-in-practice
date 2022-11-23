class BinaryHeap:
    def __init__(self, arr: list) -> None:
        self.elements = arr.copy()
        
    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.elements)
    
    def peek(self):
        if self.isEmpty():
            print("No Such Element Exception")
            return
        
        return self.elements[0]
    
    def insertMin(self, i):
        temp = self.elements[i] # insert element
        p = (i-1)//2 # p is i's parent node index is (i-1//2) ps. i-index node
        while i > 0 and temp < self.elements[p]:
            self.elements[p] = self.elements[i]
            i = p
            p = (i-1)// 2        
        self.elements[i] = temp
    
    def insertMax(self, i):
        temp = self.elements[i] # insert element
        p = (i-1)//2 # p is i's parent node index is (i-1//2) ps. i-index node
        while i > 0 and temp > self.elements[p]:
            # self.elements[p], self.elements[i] = self.elements[i], self.elements[p]
            self.elements[i] = self.elements[p]
            i = p
            p = (i-1)// 2        
        self.elements[i] = temp

    def delMin(self, last):
        temp = self.elements[-1] # last element
        k = 0 # k is current'index node 
        self.elements[last] = self.elements[0]
        left = 2*k+1 
        found = False
        
        while left <= last and not found:
            right = left if left+1 >= last else left+1
            min = left if self.elements[left] < self.elements[right] else right
            
            if self.elements[min] < temp:
                self.elements[k] = self.elements[min]
                k = min
                left = 2*k+1
            else:
                found = True
        self.elements[k] = temp
                
                
            
def insertMinHeap(h, i):
    """insertMinHeap"""
    print('insert', h[i], 'at index', i, end = '      ')
    print(h)
    insertEle= h[i]
    fi= (i-1)//2
    while i> 0  and insertEle > h[fi] :
        h[i] = h[fi]
        i= fi
        fi= (i-1)//2
    h[i] = insertEle

def delMin(h, last):
    print('delMin', h[0], 'last index = ', last, end = '      ')
    print(h)
    insertEle= h[last]
    h[last] = h[0] #inplacesort the root
    hole = 0
    ls= hole*2+1 # left son indicies
    found = False
    while ls< last and not found:
        rs= ls if ls+1 >= last else ls+1
        min = ls if h[ls] < h[rs] else rs # minsonindex 
        if h[min] < insertEle:
            h[hole] = h[min] # promote small son up to hole
            hole = min # going down the tree
            ls= hole*2+1
        else:
            found = True
    h[hole] = insertEle      
      
if __name__ == "__main__":
    arr = [30, 85, 97, 100, 200]
    heapMin = BinaryHeap(arr)
    heapMax = BinaryHeap(arr)
    
    l = len(arr)
    for i in range(l):
        heapMin.insertMin(i)
    
    for i in range(l):
        heapMax.insertMax(i) 
            
    for i in range(l):
        insertMinHeap(arr,i)
    print(arr)
    # print(heapMin.elements)
    # heapMin.delMin(l-1)
    # print(heapMin.elements)
    # print(heapMax.elements)
    delMin(arr, l-1)
    print(arr)
    
            
    