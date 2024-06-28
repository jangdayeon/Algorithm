from collections import deque

def solution(land):
    visited = [[-1] * len(land[0]) for _ in range(len(land))] #시추번호
    dfs = deque([])
    drt = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
    visited_idx = 0 # visited 번호 부여
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1 and visited[i][j] == -1 : #석유O & 방문 안한 곳이라면
                dfs.append((i,j))
                
                depth = 0
                where = [(i,j)]
                visited_idx += 1
                while dfs:
                    a,b = dfs.pop()
                    for (aa,bb) in drt:
                        if (-1<a+aa<len(land)) and (-1<b+bb<len(land[0])) :
                            if land[a+aa][b+bb] == 1 and visited[a+aa][b+bb] == -1 :
                                dfs.append((a+aa,b+bb))
                                where.append((a+aa,b+bb))
                                depth += 1
                                visited[a+aa][b+bb] = visited_idx
                                
                if len(where) == 1:
                    land[where[0][0]][where[0][1]] = 1
                    visited[where[0][0]][where[0][1]] = visited_idx
                else:
                    for a,b in where:
                        land[a][b] = depth
                        

    result = 0             
    for sichu in range(len(land[0])):
        done = []
        total = 0
        for j in range(len(land)):
            if (visited[j][sichu] not in done) and land[j][sichu] > 0 :
                total += land[j][sichu]
                done.append(visited[j][sichu])
        if total > result :
            result = total

    return result