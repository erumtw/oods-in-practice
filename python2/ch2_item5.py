
def bon(w):
    az = list('abcdefghijklmnopqrstuvwxyz')
    w_set = set(w)
    
    for c in w_set:
        if w.count(c) > 1:
            x = az.index(c) + 1
            return (x + x) * 2
 
secretCode = input("Enter secret code : ")
print(bon(secretCode))