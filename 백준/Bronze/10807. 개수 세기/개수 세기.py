import sys

input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))

what = int(input())

rst = 0
for i in range(n):
    if(li[i]==what):
       rst+=1
print(rst)