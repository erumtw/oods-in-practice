# descending sort
# 5 4 3 2 1
def ReverseSort(arr, i, j, isSorted):
    n = len(arr) 
    if n < 2:
        return
    if i <= n-1:
        if isSorted == n-1:
            return arr
        
        if j == n-1:
            isSorted = 0
            ReverseSort(arr, 0, 0, isSorted) 
        elif arr[i] >= arr[i+1]: # check if sorted
            isSorted += 1
            return ReverseSort(arr, i+1, i+1, isSorted)
        else:
            if arr[j] < arr[j+1]:
                # swap
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                return ReverseSort(arr, j+1, j+1, 0)
            elif arr[j] > arr[j+1]:
                return ReverseSort(arr, 0, 0, 0)
    else:
        return


if __name__ == '__main__':
    arr = input("Enter your List : ").split(',')
    arr = [int(e) for e in arr]
    ReverseSort(arr, 0, 0, 0)
    print("List after Sorted :", arr)
