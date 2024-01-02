import sys
input = sys.stdin.readline

n,m = map(int, input().split())
bucket = [0 for _ in range(n)]

for i in range(m):
    a,b,c = map(int, input().split())
    for j in range(a-1,b):
        bucket[j]=c

for i in range(n):
    print(bucket[i],end=' ')