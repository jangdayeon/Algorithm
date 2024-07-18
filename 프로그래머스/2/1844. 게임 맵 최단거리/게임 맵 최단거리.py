from collections import deque
def solution(maps):
    q = deque([(0,0)])
    visited = [[-1] * len(maps[0]) for _ in range(len(maps))]
    visited[0][0] = 1
    dirt = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
    while q:
        n_i,n_j = q.popleft()
        for (d_i, d_j) in dirt:
            if -1<n_i+d_i<len(maps) and -1<n_j+d_j<len(maps[0]) and visited[n_i+d_i][n_j+d_j] == -1 and maps [n_i+d_i][n_j+d_j] == 1 :
                visited[n_i+d_i][n_j+d_j] = visited[n_i][n_j] + 1
                q.append((n_i+d_i,n_j+d_j))
                if n_i+d_i == len(maps)-1 and n_j+d_j == len(maps[0])-1 :
                    return visited[len(maps)-1][len(maps[0])-1]
    return -1
            
                