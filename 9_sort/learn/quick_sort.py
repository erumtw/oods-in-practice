def quickSort(arr):
    qSortR(arr, 0, len(arr)-1)
    
def qSortR(arr, left, right):
    if left < right:
        # j = partition(arr, left, right)
        # j = partition2(arr, left, right)
        j = partition3(arr, left, right)
        qSortR(arr, left, j-1)
        qSortR(arr, j+1, right)
        
# p = left of arr
def partition(arr, left, right):
    p = arr[left]
    i, j = left+1, right
    while i < j:
        while arr[i] < p:
            i += 1
            if i == right:
                break
        while p < arr[j]:
            j -= 1
            if j == left:
                break
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], p
    return j

# p = right of arr
def partition2(arr, left, right):
    p = arr[right]
    i, j = left, right-1
    while i < j:
        while arr[i] < p:
            i += 1
            if i == right:
                break
        while p < arr[j]:
            j -= 1
            if j == left:
                break
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[right], arr[i] = arr[i], p
    return i

def partition3(arr, left, right):
    c = (left+right) // 2
    if arr[left] < arr[c]:
        arr[left], arr[c] = arr[c], arr[left]
    if arr[right] < arr[c]:
        arr[right], arr[c] = arr[c], arr[right]
    if arr[right] < arr[left]:
        arr[right], arr[left] = arr[left], arr[right]
        
    p = arr[left]
    i, j = left+1, right-1
    while i < j:
        while p < arr[j]:
            j -= 1
            # if j == left:
            #     break
        while arr[i] < p:
            i += 1
            # if i == right:
            #     break
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[left], arr[j] = arr[j], p
    return j


arr=[8, 2, 5, 7, 900, 1, 6, 10, 0, 11, 200,101,102,105,99,85,56,521,654,465,4,418,4,54,84]
print(arr)
quickSort(arr)
print(arr)