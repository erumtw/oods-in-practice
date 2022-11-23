def powerset(nums):
    # abrar (2020, yt.com/c/abrarisme)
    result = []
    partial = []

    def directed_powerset(ind):
        if ind == len(nums):
            result.append(partial[:])
            return
        partial.append(nums[ind])
        directed_powerset(ind + 1)
        partial.pop()
        directed_powerset(ind + 1)

    directed_powerset(0)
    return result

def bubble_sort(arr):
    l = len(arr) 
    for i in range(l-1):
        for k in range(l-i-1):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]

def bubble_sortVolume(arr):
    l = len(arr) 
    for i in range(l-1):
        for k in range(l-i-1):
            if len(arr[k]) > len(arr[k+1]):
                arr[k], arr[k+1] = arr[k+1], arr[k]

def sortinside(arr):
    l = len(arr) 
    for i in range(l-1):
        for k in range(l-i-1):
            n = 0      
            if arr[k][n] == arr[k+1][n]:
                n += 1
            if arr[k][n] > arr[k+1][n]:
                arr[k], arr[k+1] = arr[k+1], arr[k]

            
                
if __name__ == "__main__":                
    inp = input("Enter Input : ").split("/")
    arr = [ int(e) for e in inp[1].split() ]
    powerset = powerset(arr)
    result = []
    
    for i in range(len(powerset)):
        if sum(powerset[i]) == int(inp[0]) :
            bubble_sort(powerset[i])
            result.append(powerset[i])
    
    sortinside(result)
    bubble_sortVolume(result)

    if result == []:
        print("No Subset")
    else:
        for e in result:
            print(e)
        