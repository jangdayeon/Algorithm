def solution(n):
    nCount1 = format(n,'b').count('1')
    for i in range(n+1,1000001):
        a = format(i,'b')
        if str(a).count('1') == nCount1:
            return i