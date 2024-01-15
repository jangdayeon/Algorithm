import sys
input = sys.stdin.readline

n,m = map(int, input().split())
ls = [i for i in range(1,n+1)]

for i in range(m):
    a,b = map(int, input().split())
    new_ls = [ls[j] for j in range(a-1,b)]
    new_ls.reverse()
    idx=0
    for j in range(a-1,b):
        ls[j] = new_ls[idx]
        idx+=1
    
        
for i in range(n):
    print(ls[i], end=" ")