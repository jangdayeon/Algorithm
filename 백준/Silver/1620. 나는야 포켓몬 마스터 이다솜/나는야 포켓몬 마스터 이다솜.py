import sys
input = sys.stdin.readline

n,m = map(int, input().split())
dic = dict()
cnt = 0
for i in range(1,n+1):
    cnt+=1
    a = input().strip()
    dic[cnt] = a
    dic[a] = cnt

for _ in range(m):
    a = input().strip()
    if(a.isdigit()):
        print(dic[int(a)])
    else:
        print(dic[a])