#bfs
#한 번 틀림. 답 확인. L을 향해 갈 때 E를 지나칠 수 있다는 것을 간과
from collections import deque
def solution(maps):
    tmp_maps = []
    for i in range(len(maps)):
        maps[i] = list(maps[i])
        tmp_maps.append(list(maps[i]))
        
    dirt = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
    q = deque([])
    lever = ()
    #레버 찾기
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                tmp_maps[i][j] = 'O' #레버 -> exit 갈 때 사용할 배열의 start 지점 O으로 변경
                q.append((i,j))
                maps[i][j] = 0
                while q :
                    now_i, now_j = q.popleft()
                    for (d_i,d_j) in dirt:
                        if -1<now_i+d_i<len(maps) and -1<now_j+d_j<len(maps[0]) :
                            if maps[now_i+d_i][now_j+d_j] in ['O','E']:
                                q.append((now_i+d_i,now_j+d_j))
                                maps[now_i+d_i][now_j+d_j] = maps[now_i][now_j] + 1 
                            elif maps[now_i+d_i][now_j+d_j] == 'L':
                                maps[now_i+d_i][now_j+d_j] = maps[now_i][now_j] + 1
                                lever = (now_i+d_i, now_j+d_j)
                                tmp_maps[now_i+d_i][now_j+d_j] = maps[now_i+d_i][now_j+d_j] #레버 값 지정
                                break
    #레버 못 찾았으면 -1 리턴                      
    if not lever : return -1

    #Exit 찾기
    q = deque([])
    maps = tmp_maps
    print(maps)
    q.append(lever)
    while q :
        now_i, now_j = q.popleft()
        for (d_i,d_j) in dirt:
            if -1<now_i+d_i<len(maps) and -1<now_j+d_j<len(maps[0]) :
                if maps[now_i+d_i][now_j+d_j] == 'O':
                    q.append((now_i+d_i,now_j+d_j))
                    maps[now_i+d_i][now_j+d_j] = maps[now_i][now_j] + 1 
                elif maps[now_i+d_i][now_j+d_j] == 'E':
                    return maps[now_i][now_j] + 1  
    return -1