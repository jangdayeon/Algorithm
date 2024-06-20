def solution(n):
    li = [i for i in range(0,n+1)]
    for i in range(1,len(li)):
        li[i] += li[i-1]
    l = 0
    r = 1
    cnt = 0
    while l <= n and r <= n :
        if li[r] - li[l] < n :
            r += 1
        else :
            if li[r] - li[l] == n :
                cnt += 1
            l += 1
    return cnt