import math
def solution(n):
    sosu = [True] * (n+1)
    sosu[0], sosu[1] = False, False
    for i in range(2, n+1):
        for j in range(2,math.ceil((n+1)/i)):
            sosu[i*j] = False
    
    result = 0
    for i in range(1,n+1):
        if sosu[i]:
            result+=1
    return result