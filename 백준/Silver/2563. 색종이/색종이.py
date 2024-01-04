import sys
input = sys.stdin.readline

n = int(input())

p = [[0 for _ in range(100)] for _ in range(100)]

for i in range(n):
    x,y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            p[x-1+j][y-1+k] = 1
    
rst = 0
for i in range(100):
    rst+=p[i].count(1)
print(rst)