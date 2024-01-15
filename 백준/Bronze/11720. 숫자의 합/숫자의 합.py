import sys
input = sys.stdin.readline

n = int(input())
l = input().strip()
sum = 0
for i in range(len(l)):
    sum+=int(l[i])
print(sum)
    