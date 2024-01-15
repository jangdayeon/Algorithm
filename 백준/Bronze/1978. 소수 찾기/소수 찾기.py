import sys
input = sys.stdin.readline

n = int(input())
rst = 0
a = list(map(int, input().split()))
for i in a:
    chk = True
    if(i==1):
        continue
    for j in range(2,i):
        if(i%j==0):
            chk = False
            break
    if(chk == True):
        rst+=1
    chk = True
    
print(rst)