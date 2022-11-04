def isSorted(arr):
    i = len(arr)-1

    if i == 1:
        return True
    
    if arr[i] < arr[i-1]:
        return False
    
    isSorted(arr[:i])    

    return True

inp =[int(c) for c in input("Enter Input : ").split()] 

print("Yes") if isSorted(inp) else print("No")