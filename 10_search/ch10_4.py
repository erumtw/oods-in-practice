class Hash:
    def __init__(self, tableSize, maxCollision, threshold) -> None:
        self.tableSize = int(tableSize)
        self.maxCollision = int(maxCollision)
        self.threshold = int(threshold)
        self.size = 0
        self.hashTable = [None] * self.tableSize
        
    def hf(self, key):
        return key % self.tableSize
    
    def insert(self, key):
        # insertion
        if key < 0 or self.isExisted(key):
            return
        
        self.size += 1
        if self.isOverLoad():
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash()
            self.insert(key)
            return
        
        idx = self.hf(key) # hashing
        if self.hashTable[idx] is None:
            self.hashTable[idx] = key
            return
        
        # occured collision
        newIdx = self.QuadraticProbing(idx)
        if newIdx == -1 :
            self.rehash()
            return self.insert(key)
        self.hashTable[newIdx] = key
            # self.insert(key)
            # return 
        # return self.insert(key)
    
    def isOverLoad(self):
        # check threshhold
        curThreshold = (self.size/self.tableSize) * 100
        return curThreshold > self.threshold
    
    def isExisted(self, key):
        for e in self.hashTable:
            if e != None and key == e :
                return True
        return False
     
    def QuadraticProbing(self, index):
        # newIdx = index
        collision = 0
        
        for i in range(self.tableSize):
            newIdx = (index + i**2) % self.tableSize
            if self.hashTable[newIdx] is None:
                break
            
            collision += 1
            print(f'collision number {collision} at {newIdx}')
            
            if collision == self.maxCollision:
                print('****** Max collision - Rehash !!! ******')
                return -1
            
        return newIdx
    
    def rehash(self):
        oldTable = self.hashTable
        
        def isPrime(num):
            if num > 1:
                for i in range(2, int(num/2)+1):
                    if (num % i) == 0:
                        return False
                else:
                    return True
            else:
                return False
        
        newSize = self.tableSize * 2
        while True:
            if isPrime(newSize):
                break
            newSize += 1
        
        self.tableSize = newSize
        self.size = 0
        self.hashTable = [None] * self.tableSize
        
        # hash old to new
        for e in reversed(oldTable):
            if e != None:
                self.insert(e)  
        
        
    def printTable(self) -> str:
        for i in range(self.tableSize):
            print(f"#{i+1}	{self.hashTable[i]}")
            
"""
ให้น้องๆเขียนการทำ Rehashing ด้วยเงื่อนไขดังนี้
1. Table เต็มถึงระดับที่กำหนด ( Threshold (%) )
2. เมื่อเกิดการ Collision ถึงจำนวนที่กำหนด
""" 

if __name__ == '__main__':
    print(" ***** Rehashing *****")
    inp = input("Enter Input : ").split('/')
    tableSize, maxCollision, threshold = inp[0].split()
    hashTable = Hash(tableSize, maxCollision, threshold)
    
    print("Initial Table :")
    hashTable.printTable()
    print("----------------------------------------")
    
    for key in inp[1].split():
        if hashTable.size == hashTable.tableSize:
            print("This table is full !!!!!!")

        print(f"Add : {key}")
        hashTable.insert(int(key))
        hashTable.printTable()
        print("----------------------------------------")