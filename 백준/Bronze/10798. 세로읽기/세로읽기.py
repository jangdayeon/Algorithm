import sys
input = sys.stdin.readline

a = [[] for _ in range(5)]
m = 0
for i in range(5):
    a[i] = list(input().strip())
    m = max(m, len(a[i]))


for i in range(m):
    for j in range(5):
        if(len(a[j])<=i):
            continue
        else:
            print(a[j][i], end='')