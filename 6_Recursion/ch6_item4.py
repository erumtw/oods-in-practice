# N ชนิด
# S sourness -> s1 * s2 * sN
# B bitterness ->  b1 + b2 + bN

def perket(N, i=None, result=None):
    i = 0 if i == None else i
    result = [] if result == None else result
    
    if i < len(N):
        if N[i] != []:
            result.append(abs(sourness(N[i]) - bitterness(N[i])))
            return perket(N, i+1, result)
        
    return min(result)

def powerset(nums):
    # abrar (2020, yt.com/c/abrarisme)
    result = []
    partial = []
    def directed_powerset ( ind ):
        if ind == len ( nums ):
            result.append (partial [:])
            return
        partial.append (nums[ind])
        directed_powerset (ind + 1)
        partial.pop ()
        directed_powerset (ind + 1)
       
    directed_powerset (0)
    return result

def sourness(s, n=None):
    n = 0 if n == None else n
    if n < len(s) - 1:
        return int(s[n].split()[0])  * int(sourness(s, n+1))
    else: 
        return int(s[n].split()[0]) 
    
def bitterness(s, n=None):
    n = 0 if n == None else n
    if n < len(s) - 1:
        return int(s[n].split()[1]) + int(bitterness(s, n+1))
    else: 
        return int(s[n].split()[1])

if __name__ == '__main__':
    inp = input("Enter Input : ").split(',')
    N = powerset(inp)
    # print(N)
    # print(sourness(N[0]))
    print(perket(N))