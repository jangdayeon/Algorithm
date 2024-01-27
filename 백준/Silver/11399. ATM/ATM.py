import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li.sort()
rst = 0
for i in range(n):
    rst += sum(li[:i+1:])
print(rst)