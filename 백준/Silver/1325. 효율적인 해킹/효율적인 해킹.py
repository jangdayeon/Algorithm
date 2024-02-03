import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
li = [[None] for _ in range(n+1)]
for i in li:
    i.remove(None)
visited = [False] * (n+1)

for i in range(m):
    a,b = map(int, input().split()) #b가 부모, a가 자식
    li[b].append(a) #부모에 자식추가

rtn = 0
def bfs(start):
    queue = deque([start])
    global rtn
    visited[start] = True
    while queue:
        v = queue.popleft()
        rtn +=1
        for i in li[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return rtn

rst = [0 for _ in range(n+1)]

for i in range(1,len(li)):
    visited = [False] * (n+1)
    rtn = 0
    if(len(li[i])!=0):
        rst[i] = bfs(i)
rst2 = []
for i in range(len(rst)):
    if(rst[i]==max(rst)):
        rst2.append(i)
print(*rst2)