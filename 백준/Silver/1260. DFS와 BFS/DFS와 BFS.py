import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

n,m,v = map(int, input().split()) #정점의 개수, 간선의 개수, 탐색을 시작할 정점
mmm = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    mmm[a].append(b)
    mmm[b].append(a)
for i in range(1,n+1):
    mmm[i].sort()

def dfs(start):
    print(start, end=' ')
    visited[start] = True
    for i in mmm[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    visited[start] = True
    queue = deque([start])
    while queue:
        q = queue.popleft()
        print(q, end=' ')
        for i in mmm[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(v)
print()
visited = [False for _ in range(n+1)]
bfs(v)