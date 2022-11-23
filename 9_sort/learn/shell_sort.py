# base on insertion sort but faster
# by split out of h group and do insert sort and merge them, then do insert sort again

def shell_sort(arr):
    n= 3
    for h in range(n, 0, -1):
        for m in range(h):
            l = len(arr)
            for k in range(h+m, l, h):
                temp = arr[k]
                prev_k = k-h
                while prev_k >= 0 and temp < arr[prev_k]:
                    arr[prev_k], arr[prev_k+h] = arr[prev_k+h], arr[prev_k]
                    prev_k -= h 
                arr[prev_k+h] = temp

arr=[8, 2, 5, 7, 900, 1, 6, 10, 0, 11, 200,101,102,105,99,85,56,521,654,465,4,418,4,54,84]
print(arr)
shell_sort(arr)
print(arr)

