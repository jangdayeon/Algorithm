import sys
input = sys.stdin.readline

li = []
for i in range(9):
    li.append(int(input()))

print(max(li))
print(li.index(max(li))+1)