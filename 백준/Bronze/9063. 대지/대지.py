import sys
input = sys.stdin.readline

n = int(input())

x = []
y = []
for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
rst = (max(x)-min(x))*(max(y)-min(y))
print(rst)