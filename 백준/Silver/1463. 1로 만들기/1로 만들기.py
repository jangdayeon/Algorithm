import sys
input = sys.stdin.readline

n = int(input())

num = [0] * (n+1)
num[1] = 0
for i in range(2,n+1):
    chk = []
    for j in [2,3]:
        if(i%j==0):
            chk.append(num[i//j])
    chk.append(num[i-1])
    num[i] = min(chk)+1
    
print(num[n])