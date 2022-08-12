def range(*args): 
    start , end  , step = 0, 0, 1
    if(len(args) == 1):
         start , end = 0, args[0]      
    elif(len(args) == 2):
         start , end  = args[0], args[1]   
    elif(len(args) == 3):
         start, end , step = args[0], args[1], args[2]
    else:
        return None
    
    lists = []
    i = start
    while i < end:
        lists.append(round(float(i), 5))
        i += step
        
    return tuple(lists)

print('*** New Range ***')
inputs = input("Enter Input : ").split()
if(len(inputs) == 1):
     print(range(float(inputs[0])))
elif(len(inputs) == 2):
     print(range(float(inputs[0]), float(inputs[1])))
elif(len(inputs) == 3):
     print(range(float(inputs[0]), float(inputs[1]), float(inputs[2])))
else:
     pass

