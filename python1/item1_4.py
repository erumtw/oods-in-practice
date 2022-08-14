# สร้างฟังก์ชันที่รับ input เป็น list(5x5) ของ # และ -
# โดยแต่ละแฮช (#) แทนทุ่นระเบิดและแต่ละขีด (-) แทนจุดที่ไม่มีทุ่นระเบิด
# ให้ return list ที่แต่ละขีดถูกแทนที่ด้วยตัวเลขที่ระบุจำนวนของทุ่นระเบิดที่อยู่ติดกับจุดนั้น (แนวนอนแนวตั้งและแนวทแยงมุม)

def num_grid(lst):
    lst_len = len(lst)

    # Code Here
    for i in range(lst_len):
        for j in range(lst_len):
            # initial c for count
            c = 0
            # top check
            if lst[i][j] != '#':
                if i != 0 and lst[i-1][j] == '#':
                    c += 1
                # bottom check
                if i != lst_len - 1 and lst[i+1][j] == '#':
                    c += 1
                # left check
                if j != 0 and lst[i][j-1] == '#':
                    c += 1
                # right check
                if j != lst_len - 1 and lst[i][j+1] == '#':
                    c += 1
                # top left
                if i != 0 and j != 0 and lst[i-1][j-1] == '#':
                    c += 1
                # top right
                if i != 0 and j != lst_len - 1 and lst[i-1][j+1] == '#':
                    c += 1
                # bottom left
                if j != 0 and i != lst_len - 1 and lst[i+1][j-1] == '#':
                    c += 1
                # bottom right
                if j != lst_len - 1 and i != lst_len-1 and lst[i+1][j+1] == '#':
                    c += 1
                    
                lst[i][j] = str(c)

    return lst


'''lst_input = [

    ["-","-","-","-","-"],

    ["-","-","-","-","-"],

    ["-","-","#","-","-"],

    ["-","-","-","-","-"],

    ["-","-","-","-","-"]

]'''

lst_input = []
print("*** Minesweeper ***")

input_list = input("Enter input(5x5) : ").split(",")

for e in input_list:
    lst_input.append([i for i in e.split()])

print("\n", *lst_input, sep="\n")

print("\n", *num_grid(lst_input), sep="\n")
