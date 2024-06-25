def solution(n):
    a = 1
    b = 2
    if n < 3 :
        if n == 1 : return 1
        else : return 2
    for i in range(3,n+1):
        a,b = b,a+b
    return b%1234567