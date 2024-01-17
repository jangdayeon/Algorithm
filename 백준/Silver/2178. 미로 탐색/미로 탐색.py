import sys
input= sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
pan = [[] for _ in range(n)]
for j in range(n):
    pan[j] = list(map(int, list(input().strip())))

wh = [[-1,0],[1,0],[0,-1],[0,1]] # 상,하,좌,우
def bfs():
    queue = deque([[0,0]])
    while queue:
        a,b = map(int, queue.popleft())
        for i in range(4):
            where = wh[i]
            if(a+where[0]>-1 and a+where[0]<n and b+where[1]>-1 and b+where[1]<m):
                if(pan[a+where[0]][b+where[1]]==1):
                    pan[a+where[0]][b+where[1]]=pan[a][b]+1
                    queue.append([a+where[0],b+where[1]])
    return pan[n-1][m-1] 

print(bfs())