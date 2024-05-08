def solution(n):
    a = 0
    b = 1
    for i in range(2,n+1):
        if i%2==0:
            a = (a+b)%1234567
        else:
            b = (b+a)%1234567
    return a%1234567 if n%2==0 else b%1234567
    