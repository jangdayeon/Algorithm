import sys
input = sys.stdin.readline

n,m = map(int, input().split())

bucket = [i for i in range(1,n+1)]

for i in range(m):
    a,b = map(int, input().split())
    tmp = bucket[a-1]
    bucket[a-1]=bucket[b-1]
    bucket[b-1]=tmp

for i in range(n):
    print(bucket[i], end=' ')