import sys
input = sys.stdin.readline

n = [[] for _ in range(9)]

m = [-1 for _ in range(3)]
for i in range(9):
    n[i] = list(map(int, input().split()))
    if(m[0]<max(n[i])):
        m[0] = max(n[i])
        m[1] = i+1
        m[2] = n[i].index(m[0]) +1
print(m[0])
print(m[1], m[2])