import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int, input().split()) #정점개수, 간선개수
pan =[[] for _ in range(n+1)]
chk =[False for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, input().split())
    pan[u].append(v)
    pan[v].append(u)

#여기까지 데이터 입력 끝
rst = 0
def dfs(q):
    chk[q] = True
    for i in pan[q]:
        if not chk[i]:
            dfs(i)
for i in range(1,len(chk)):
    if(chk[i]==False):
        dfs(i)
        rst+=1
print(rst)