def minW(l,n):
    m = 999999
    if n==1:return sum(l)
    for i in range(len(l)):
        if len(l[i:]) < n-1:break
        m  = min(m,max(sum(l[:i]), minW(l[i:],n-1)))
    return m

l,n = input("Enter Input : ").split("/")
print("Minimum weigth for",int(n),"box(es) =",minW([int(i)for i in l.split()],int(n)))