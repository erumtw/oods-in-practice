# อยากให้นักศึกษาช่วยหาลำดับการ Countdown จาก Input ที่รับเข้ามา 
# โดยลำดับการ Countdown จะเป็นเลขเรียงลำดับ เช่น 2->1 , 3->2->1 
# โดยจะสิ้นสุดด้วย 1 เสมอ
# โดยผลลัพธ์ให้แสดง List ของ จำนวนลำดับที่เจอ และ แต่ละลำดับเป็นอย่างไร

def getCountdownList(lst):
    isCd = False
    count = 0
    cdlist = []
    l = []
    
    for i in range(len(lst)):
        if lst[i] == 1:
            if i == 0:
                count += 1
                cdlist.append([lst[i]])
            elif lst[i] == 1 and lst[i-1] == 1:
                count += 1
                cdlist.append([lst[i]])
            elif lst[i] == 1 and isCd == True:
                l.append(lst[i])
                count += 1
                cdlist += [l.copy()]
                l.clear()
        elif i != len(lst)-1 and lst[i+1] == lst[i] - 1:
            isCd = True
            l.append(lst[i])
        else:
            isCd = False
            l.clear()
            
    return [count, cdlist]
            

print("*** Fun with countdown ***")
l = input('Enter List : ').split()
int_l = [ int(e) for e in l ]
print(getCountdownList(int_l))
