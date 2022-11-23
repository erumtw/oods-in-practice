def bubble_sort(arr):
    l = len(arr)
    
    for j in range(l-1):
        for i in range(l-j-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    
    return arr
    
    
    
    
if __name__== "__main__":
    l = [e for e in input("Enter Input : ").split()]
    if l[0] == 'EX':
        Ans = "Quick Sort"
        print("Extra Question : What is a suitable sort algorithm?")
        print("   Your Answer : "+Ans)
    else:
        l=list(map(int, l))
        #code here
        median = 0
        for n in range(len(l)):
            for i in range(len(l)):
                if i == n :
                    mid = i//2 
                    l2 = bubble_sort(l.copy()[:i+1])
                    if (i+1) % 2 == 0:
                        median = (l2[mid]+l2[mid+1]) / 2
                    else:
                        median = l2[mid]
                    print(f"list = {l[:i+1]} : median = {median:.1f}")
                    break