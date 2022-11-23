def insert_sort(arr):
    l = len(arr)
    for k in range(1, l):
        temp = arr[k]
        prev_k = k-1
        while prev_k >= 0 and temp < arr[prev_k]:
            arr[prev_k], arr[prev_k+1] = arr[prev_k+1], arr[prev_k]
            prev_k -= 1
        arr[prev_k+1] = temp
        
        
arr=[8, 2, 5, 7, -900, 1, 6, -10, 0, 11, 200]
print(arr)
insert_sort(arr)
print(arr)