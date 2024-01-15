import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

rst = []
for i in range(m,n+1):
    chk = True
    if(i==1):
        continue
    for j in range(2,i):
        if(i%j==0):
            chk=False
            break
    if(chk==True):
        rst.append(i)
    chk=True

if (len(rst)!=0):
    print(sum(rst))
    print(rst[0])
else:
    print(-1)