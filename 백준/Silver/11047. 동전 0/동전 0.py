import sys
input= sys.stdin.readline

n,k = map(int, input().split())
won = []
for i in range(n):
    won.append(int(input()))
won= sorted(won, reverse=True)
rst = 0
for i in won:
    if(k==0):
        break
    if(k>=i):
        rst+=k//i
        k -= (k//i)*i 
print(rst)