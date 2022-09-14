def sortedR(arr):
    for i, e in enumerate(arr):
        j = i+1
        if j < len(arr)-1 :
            while e < arr[j]:
                j += 1
            if e < arr[j]:
                swap(arr[i], arr[j])
        

def swap(a, b):
    temp = b
    a = b
    b = temp


if __name__ == '__main__':
    arr = input("Enter your List : ").split()
    arr = [int(e) for e in arr]
    sortedR(arr)
    print(arr)
