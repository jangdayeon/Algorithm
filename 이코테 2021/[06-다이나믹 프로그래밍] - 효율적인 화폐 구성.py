import sys
input = sys.stdin.readline

n,m = map(int, input().split()) #n가지 종류의 화폐, 합 m
danwe = []
for _ in range(n):
    danwe.append(int(input()))

x = [-1] * 10000
for i in danwe:
    x[i] = 1
for i in range(min(danwe), m+1):
    for j in danwe:
        if((i-j)>-1):
            if( x[i-j]!=-1):
                x[i] = x[i-j]+1

print(x[m])

#점화식 a_n = min(a_n-3, a_n-2)+1 #단위가 2,3이 있을 때