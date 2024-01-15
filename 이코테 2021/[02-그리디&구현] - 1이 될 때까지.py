import sys
input= sys.stdin.readline

n,k = map(int, input().split())
rest = n
rst = 0
while(rest>1):
    if(rest%k==0):
        rst+=1
        rest = rest//k
    else:
        rst+=1
        rest-=1
print(rst)