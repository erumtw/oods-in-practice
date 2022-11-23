def mergeSort(arr):
    mergeR(arr, 0, len(arr)-1, arr.copy())
    
def mergeR(a, left, right, b):
    if left < right:
        mid = (left+right)//2
        mergeR(b, left, mid, a)
        mergeR(b, mid+1, right, a)
        merge(b, left, mid, right, a)

def merge(a, left, mid, right, b):
    i, j = left, mid+1
    for k in range(left, right+1):
        if i > mid:
            b[k] = a[j] 
            j+=1
            continue
        
        if j > right:
            b[k] = a[i] 
            i+=1
            continue

        if a[i] < a[j]:
            b[k] = a[i]
            i+=1
        else:
            b[k] = a[j]
            j+=1
    
arr=[8, 2, 5, 7, 900, 1, 6, 10, 0, 11, 200,101,102,105,99,85,56,521,654,465,4,418,4,54,84]
print(arr)
mergeSort(arr)
print(arr)