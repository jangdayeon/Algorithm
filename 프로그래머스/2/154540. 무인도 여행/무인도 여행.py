#dfs
from collections import deque
def solution(maps):
    maps,visited = mapsSetting(maps)
    dirt = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
    q = deque([])
    result = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j]:
                food = 0
                q.append((i,j))
                while q:
                    nowA,nowB = q.popleft()
                    if visited[nowA][nowB]:
                        continue
                    visited[nowA][nowB] = True
                    food+=maps[nowA][nowB]
                    for a,b in dirt:
                        if -1<nowA+a<len(maps) and -1<nowB+b<len(maps[0]) and not visited[nowA+a][nowB+b]:
                            q.append((nowA+a,nowB+b))
                result.append(food)
    return [-1] if not result else sorted(result)
                            
def mapsSetting(maps):
    maps=list(map(lambda x:list(x),maps))
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'X':
                maps[i][j] =-1
                visited[i][j] = True
            else:
                maps[i][j] = int(maps[i][j])
    return (maps,visited)