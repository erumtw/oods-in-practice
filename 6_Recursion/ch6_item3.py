def gcd(a, b): 
    if b != 0:
        return gcd(b, a%b)
    else:
        return a if a > 0 else -a
    
    # if a == 0:
    #     return b if b > 0 else -b
    # if b == 0:
    #     return a if a > 0 else -a
    # if a == b:
    #     return b if b > 0 else -b
    
    # # q = a // b
    # # r = a - b*q
    
    # # if a == b*q:
    # #     if b < 0:
    # #         return b*-1
    # #     else:
    # #         return b
    # # else:
    # return gcd(b, a % b)
        

if __name__ == "__main__":
    a, b = input("Enter Input : ").split()
    if a == '0' and b == '0':
        print("Error! must be not all zero.")
    else:
        if int(a) < int(b):
            a, b =  b, a
        print(f"The gcd of {a} and {b} is :", gcd(int(a),int(b)))

# '''
# in -36 -24
# 36 > 24
# -36 -24

# in -24 -36
# -36 -24

# '''




# def rec_gcd(x, y):
#     if x < 0:
#         x = -x
#     if y < 0:
#         y = -y
#     if x != 0 and y == 0:
#         return x
#     elif x == 0 and y != 0:
#         return y
#     elif x == 1 or y == 1:
#         return 1
#     else:
#         if x >= y:
#             return rec_gcd(y, x % y)
#         else:
#             return rec_gcd(x, y % x)


# if __name__ == '__main__':
#     a, b = list(map(int, input('Enter Input : ').split()))
#     if a == 0 and b == 0:
#         print('Error! must be not all zero.')
#     else:
#         if a >= b >= 0 or a >= 0 >= b:
#             print(f'The gcd of {a} and {b} is : {rec_gcd(a, b)}')
#         elif b >= a >= 0 or b >= 0 >= a:
#             print(f'The gcd of {b} and {a} is : {rec_gcd(a, b)}')
#         elif a < 0 and b < 0:
#             if abs(a) > abs(b):
#                 print(f'The gcd of {a} and {b} is : {rec_gcd(a, b)}')
#             else:
#                 print(f'The gcd of {b} and {a} is : {rec_gcd(a, b)}')