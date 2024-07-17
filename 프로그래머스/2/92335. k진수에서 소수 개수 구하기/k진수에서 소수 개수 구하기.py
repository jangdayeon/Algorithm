def solution(n, k):
    change = []
    while n > 0 :
        div, mod = divmod(n,k)
        change.append(int(mod))
        n = div
    change.reverse()
    result = 0
    start = 0
    for i,c in enumerate(change):
        if c == 0 :
            if start != i :
                result += checkSosu(change[start:i])
            start = i+1
        if i == len(change)-1 and start != i+1:
            result += checkSosu(change[start:])
    return result

def checkSosu(n):
    n = int("".join(map(lambda x:str(x), n)))
    print(n)
    if n == 1 :
        return 0
    for i in range(2,int(n**(1/2))+1):
        if n % i == 0 :
            return 0
    return 1