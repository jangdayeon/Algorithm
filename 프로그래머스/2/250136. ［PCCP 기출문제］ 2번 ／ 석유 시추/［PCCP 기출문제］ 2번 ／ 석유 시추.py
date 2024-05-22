#bfs 문제
#1. 방문한 곳은 1을 넓이로 치환해서 저장
#2. 넓이 다 구하면 왼에서 오로 이동하면서 리스트 연결되어 있지 않을 경우 + 해줌

#한 번 틀림. bfs에서 시작점 1이어서 중복 탐색되는 거를 수정함
#두 번 틀림. 답 확인. 같은 시추일 경우를 고려를 못했음.. -> unique값을 저장한 land_ukey 리스트를 만들어 해결
#세 번 틀림. 시간초과.. deepcopy 코드 삭제
from collections import deque

def solution(land):
    queue = deque([])
    
    #석유 있는 곳 queue에 저장
    for i, row in enumerate(land): 
        for j, column in enumerate(row):
            if column == 1 :
                 queue.append((i,j))
                    
    #석유 있는 곳을 bfs해서 넓이 확인
    land_ukey = [([0]*len(land[0])) for _ in land] #unique한 값 넣어줌
    ukey = 1
    for i,j in queue:
        if land[i][j] == 1:
            mustChange, cnt = bfs(i,j,land)
            for a,b in mustChange:
                land[a][b] = cnt
                land_ukey[a][b] = ukey
            ukey +=1
                
    temp = [0]
    result = 0
    ctnu_set = set([0])
    #인덱스 옮겨가며 석유 합 구함
    for j in range(len(land[0])):
        for i in range(len(land)):
            if land_ukey[i][j] not in ctnu_set :
                temp.append(land[i][j])
                ctnu_set.add(land_ukey[i][j])
        ctnu_set = set([0])
        result = max(sum(temp), result)
        temp = [0]
    return result
    
def bfs(i,j,land):
    queue = deque([(i,j)])
    mustChange = []
    direction = [(-1,0),(1,0),(0,1),(0,-1)] #상,하,좌,우
    cnt = 1
    while queue:
        va, vb = queue.popleft()
        land[va][vb] = 2
        mustChange.append((va,vb))
        for a,b in direction:
            if -1 < va+a < len(land) and -1 < vb+b < len(land[0]) and land[va+a][vb+b] == 1:
                land[va+a][vb+b] = 2
                queue.append((va+a,vb+b))
                mustChange.append((va+a,vb+b))
                cnt += 1
    return (mustChange, cnt)
    
    
        