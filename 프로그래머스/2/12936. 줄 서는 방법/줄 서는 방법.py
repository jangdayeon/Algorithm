#모음사전과 유사, 단 중복은 X
from math import factorial
def solution(n, k):
    result = []
    num = [i for i in range(1,n+1)]
    now = n-1
    while now:
        ftr = factorial(now)
        for i in range(now,-1,-1):
            if k > ftr*i:
                result.append(num[i])
                num.pop(i)
                k -= ftr*i
                break
        now -= 1
    result.append(num.pop())
    return result