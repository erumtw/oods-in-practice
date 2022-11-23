# รับจำนวนเต็มมา 1 จำนวนแล้วให้แสดงผลดังนี้

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Metadrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และมีตัวซ้ำให้แสดงผลว่า "Plaindrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Katadrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และมีตัวซ้ำให้แสดงผลว่า "Nialpdrome"

# - หาก input ที่รับมานั้นทุกหลักเป็นเลขเดียวกันหมด ให้แสดงผลว่า "Repdrome"

# - หากไม่อยู่ในเงื่อนไขด้านบนเลย ให้แสดงผลว่า "Nondrome"

# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง
def whatDROME(arr):
    case = 0
    descending = False
    ascending = False
    duplicate = False
    
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            duplicate = True
            if i == len(arr)-2:
                case = 4

        if arr[i] < arr[i+1]:
            ascending = True
            if i == len(arr)-2:
                case = 0
                
        if arr[i] > arr[i+1]:
            descending = True
            if i == len(arr)-2:
                case = 2
                
    if duplicate and ascending:
        case = 1
    if duplicate and descending:
        case = 3
    if descending and ascending:
        case = 5
    
    return case

if __name__ == '__main__':
    inp = input("Enter Input : ")
    inp = list(inp)
    case = whatDROME(inp)
    # print(case)
    if case == 0:
        print("Metadrome")
    elif case == 1:
        print("Plaindrome")
    elif case == 2:
        print("Katadrome")
    elif case == 3:
        print("Nialpdrome")    
    elif case == 4:
        print("Repdrome")
    else:
        print("Nondrome")