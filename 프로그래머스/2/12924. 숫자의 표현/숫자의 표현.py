def solution(n):
    result = 0
    for i in range(1,n+1):
        tmp = i
        for j in range(i+1,n+1):
            if tmp == n :
                result +=1
                break
            elif tmp >n :
                break
            else:
                tmp+=j
    return result+1