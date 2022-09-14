# def fibo(num):
#     # x3 = x2 + x1
#     if num <= 1:
#         return num
#     else:
#         return fibo(num-2) + fibo(num-1) 

def fibo(num, memo):
    # x3 = x2 + x1
    if num <= 1:
        return num
    if num not in memo:
        memo[num] = fibo(num-1, memo) + fibo(num-2, memo) 
    return memo[num]

n = int(input('Enter Number : '))
print(f"fibo({n}) = {fibo(n, {})}")