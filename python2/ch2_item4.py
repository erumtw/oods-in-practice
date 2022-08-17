# หาค่าฐานของอายุของน้องสายไหม ที่อายุ 20,21 ตลอดกาล

def numberToBase(n, b):
    if n == 0:
        return [0]

    digits = []

    while n:
        digits.append(int(n % b))
        n //= b

    digits = [str(i) for i in digits]
    return ''.join(digits[::-1])


def hbd(age):
    b = 2
    while True:
        if numberToBase(age, b) == '20':
            age = 20
            break
        elif numberToBase(age, b) == '21':
            age = 21
            break
        else:
            b += 1

    return f'saimai is just {age}, in base {b}!'
    ### Enter Your Code Here ###


year = input("Enter year : ")

print(hbd(int(year)))
