import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
pan = []
for _ in range(n):
    pan.append(list(map(int, input().strip())))
wh = [[-1,0],[1,0],[0,-1],[0,1]] #상,하,좌,우
def bfs(a,b):
    global rst
    queue = deque([[a,b]])
    while queue:
        v = queue.popleft()
        print(v[0], v[1])
        for i in range(4):
            where = wh[i]
            if(v[0]+where[0]>-1 and v[0]+where[0]<n and v[1]+where[1]>-1 and v[1]+where[1]<m):
                if(pan[v[0]+where[0]][v[1]+where[1]] == 1):
                    queue.append([v[0]+where[0], v[1]+where[1]])
                    pan[v[0]+where[0]][v[1]+where[1]]=pan[v[0]][v[1]]+1
                    

bfs(0,0)
print(pan)
print(pan[n-1][m-1])