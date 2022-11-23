# class ArrayUtil:
#     def __init__(self) -> None:
#         pass

#     def swap(arr:list , i, j):
#         arr[i], arr[j] = arr[j], arr[i]

#     def lessThan(a, b):
#         return a < b
     
# def selection(arr: list):
#     i = len(arr)-1
#     while i > 0:
#         m = max(arr[:i+1])
#         j = arr.index(m) 
#         arr[i], arr[j] = arr[j], arr[i]   
#         i -= 1
        
#     return arr

# def selectPure(arr):
#     i = len(arr)
#     if i == 0 :
#         return

    
#     def max(j):
#         if j > i:
#            max = arr[j]
#         if arr[j] < arr[j+1]:
#             max = max(j+1) 
#         return max
    
    
# if __name__ == "__main__":
#     s = selection([8, 2, 5, 7, 9, 1, 6, 10, 0, 11, 200])

#     print(s)

def maxs(arr, j):
    max = max_x(arr, 0, j, arr[0])
    return max

def max_x(arr, i , j, mac):
    
    if i == j:
        return mac
        
    if arr[mac] < arr[i+1]:
        # mac = arr[i+1] # get value
        mac = i+1 # get index 
    
    mac = max_x(arr, i+1, j, mac)
    
    return mac
    
def selectionPure(arr: list, i):
    if i == 1:
        return 
    
    max_value = maxs(arr, i)
    # x = arr.index(max_value)
    arr[max_value], arr[i] = arr[i], arr[max_value]
    
    selectionPure(arr, i-1)
    
m = maxs([8, 2, 5, 7, 900, 1, 1006, 10, 0, 11, 200], 9)
print(m)

arr=[8, 2, 5, 7, 900, 1, 6, 10, 0, 11, 200]

selectionPure(arr, len(arr)-1)
print(arr)