def swap(arr, i,j):
    arr[i], arr[j] = arr[j], arr[i] 
    
def bubble(arr):
    l = len(arr) 
    
    for i in range(l-1):
        for k in range(l-i-1):
            if arr[k] > arr[k+1]:
                swap(arr, k, k+1)

arr=[5,4,3,2,1]
bubble(arr)
print(arr)
        

    
    