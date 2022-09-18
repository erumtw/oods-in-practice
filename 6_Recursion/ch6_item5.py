def staircase(n, i=None):
    i = 1 if i == None else i
    result = []
    
    if n == 0:
        return print('Not Draw!')
    elif n > 0:
        if i <= n:
            print("_"*(n-i), end='')
            print("#"*(i))
            return staircase(n, i+1)
    else:
        if i <= abs(n):
            print("_"*(i-1), end='')
            print("#"*(abs(n)-(i-1)))
            return staircase(n, i+1)
        
    

staircase(int(input("Enter Input : ")))