import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy
from itertools import combinations
n,m = map(int, input().split()) #세로,가로
graph = [[] for _ in range(n)]
virus = []
wall = []
for i in range(n):
    graph[i] = list(map(int, input().split()))
    for j in range(m):
        if graph[i][j] == 0:
            wall.append((i,j))
        elif graph[i][j] == 2:
            virus.append((i,j))
wallCombi = combinations(wall,3)
# print(*wallCombi)
# print(*graph)
# print(*virus)
    
direct = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
def bfs(combi,graph):
    queue = deque(virus)
    graphCopy = deepcopy(graph)
    cnt = 0
    for i,j in combi:
        graphCopy[i][j] = 1
    while queue:
        qx, qy = queue.pop()
        for x,y in direct:
            if 0<=qx+x<n and 0<=qy+y<m:
                if graphCopy[qx+x][qy+y] == 0:
                    graphCopy[qx+x][qy+y] = 2
                    queue.append((qx+x,qy+y))
    # print(*graphCopy)
    for i in graphCopy:
        cnt += i.count(0)
        # print(i)
    return cnt

maxSafeZone = 0

for combi in wallCombi:
    maxSafeZone = max(maxSafeZone, bfs(combi,graph))
print(maxSafeZone)