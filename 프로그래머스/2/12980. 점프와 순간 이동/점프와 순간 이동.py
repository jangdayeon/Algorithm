#모르겠어서 정답확인함

def solution(n):
    result = 0
    while n >0:
        if n%2 == 0:
            n = n //2
        else:
            n = n-1
            result +=1
    return result