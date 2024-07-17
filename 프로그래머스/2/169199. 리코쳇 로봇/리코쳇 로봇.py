#bfs ( 어려움 .. )
from collections import deque
def solution(board):
    visited = [[-1] * len(board[0]) for _ in range(len(board))]
    q = deque([])
    dirt = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                q.append((i,j))
                visited[i][j] = 0
                
                while q :
                    n_i, n_j = q.popleft()
                    for d_i, d_j in dirt:
                        nd_i, nd_j = n_i+d_i, n_j+d_j
                        
                        # 미끄러지기
                        while -1<nd_i<len(board) and -1<nd_j<len(board[0]) and board[nd_i][nd_j] != 'D' :
                            nd_i, nd_j = nd_i+d_i, nd_j+d_j #벽 부딪히지 않았으면 이동
                        nd_i, nd_j = nd_i-d_i, nd_j-d_j #벽 부딪혔으니 이전값으로 변경
                        
                        
                        if visited[nd_i][nd_j] == -1 : #방문 안한 곳이면,
                            if board[nd_i][nd_j] == 'G' : #골인 위치면?
                                visited[nd_i][nd_j] = visited[n_i][n_j] + 1
                                return visited[nd_i][nd_j]
                            elif (nd_i,nd_j) != (n_i,n_j) : #아직 골인 위치 아니면 q에 현재값 추가
                                visited[nd_i][nd_j] = visited[n_i][n_j] + 1
                                q.append((nd_i,nd_j))
    return -1