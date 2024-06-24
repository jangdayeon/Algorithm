def solution(n):
    f0 = 0
    f1 = 1
    for i in range(2,n+1):
        if i%2==0:
            f0 += f1
        else :
            f1 += f0
    return f0%1234567 if n%2==0 else f1%1234567