#bfs 구현 문제 / 통로 다 구한 다음에 최솟값 리턴해야 함
from collections import deque
def solution(maps):
    direction = [(-1,0),(1,0),(0,-1),(0,1)] #상,하.좌,우
    queue = deque([(0,0)])
    n, m = len(maps), len(maps[0])
    now_distance = 0
    while queue: #bfs로 maps에서 최소값 업데이트
        now = queue.popleft()
        for d in direction:
            a, b = d[0],d[1]
            if 0 <= now[0]+a < n and 0 <= now[1]+b < m :
                if maps[now[0]+a][now[1]+b] == 1 :
                    maps[now[0]+a][now[1]+b] = maps[now[0]][now[1]] + 1
                    queue.append((now[0]+a,now[1]+b))
    
    if maps[n-1][m-1] == 1: #접근 못한 경우 ( 제한 사항에서 n ==m == 1 인 경우 제외한다고 하였기에)
        return -1
    else: #접근 한 경우
        return maps[n-1][m-1]