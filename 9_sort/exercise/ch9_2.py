def sss(arr):
    selection(arr, len(arr)-1)


def selection(arr, k):
    if k == 0:
        return 
    
    def maxx(arr, i, j, max_i=None):
        max_i = 0 if max_i == None else max_i
        if i == j:
            return max_i

        if arr[max_i] < arr[i+1]:
            max_i = i+1

        max_i = maxx(arr,i+1, j, max_i)
        
        return max_i
    
    max_i = maxx(arr, 0, k)
    arr[max_i], arr[k] = arr[k], arr[max_i]
    if arr[k] != arr[max_i]:
        print(f"swap {arr[max_i]} <-> {arr[k]} : {arr}")
    
    selection(arr, k-1)

select = [ int(c) for c in input("Enter Input : ").split()]
sss(select)
print(select)
