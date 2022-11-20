class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, tableSize, maxCollision) -> None:
        self.tableSize = int(tableSize)
        self.maxCollision = int(maxCollision)
        self.size = 0
        self.hashTable = [None] * self.tableSize
        
    def hf(self, key):
        hv = 0
        for k in key:
            hv += int(ord(k))
            
        return hv % self.tableSize
    
    def insert(self, key, value):
        idx = self.hf(key)
    
        if self.hashTable[idx] is None:
            self.hashTable[idx] = Data(key, value)
        else:
            newIdx = self.QuadraticProbing(idx)
            if newIdx == -1 :
                return
              
            self.hashTable[newIdx] = Data(key, value)
        
        self.size += 1
            
    def QuadraticProbing(self, index):
        newIdx = index
        collision = 0
        
        for i in range(self.tableSize):
            newIdx = (index + i**2) % self.tableSize
            if self.hashTable[newIdx] is None:
                break
            
            collision += 1
            print(f'collision number {collision} at {newIdx}')
            
            if collision == self.maxCollision:
                print('Max of collisionChain')
                return -1
            
        return newIdx
    
    def printTable(self) -> str:
        for i in range(self.tableSize):
            print(f"#{i+1}	{self.hashTable[i]}")
            
if __name__ == '__main__':
    print(" ***** Fun with hashing *****")
    inp = input("Enter Input : ").split('/')
    tableSize, maxCollision = inp[0].split()
    hashTable = Hash(tableSize, maxCollision)
    
    for data in inp[1].split(','):
        if hashTable.size == hashTable.tableSize:
            print("This table is full !!!!!!")
            break
        
        key, value = data.split()
        hashTable.insert(key, value)
        hashTable.printTable()
        print("---------------------------")
        
    