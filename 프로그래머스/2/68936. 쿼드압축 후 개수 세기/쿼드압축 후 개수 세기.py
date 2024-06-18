#매 라운드 별 확인해야 하는 노드를  에 넣기
#확인 완료된 것은 zero or one list에 넣기

def solution(arr):
    arr_check = [[False] * len(arr) for _ in range(len(arr))]
    total_cnt = [0,0] #압축된 0과 1의 개수
    checkPoint = len(arr)
    while True:
        
        for i in range(0, len(arr),checkPoint):
            for j in range(0,len(arr),checkPoint):
                cnt = [0,0] #0과 1 개수 저장
                if arr_check[i][j] == False: #압축 안한 곳이면?
                    for a in range(i,i+checkPoint):
                        for b in range(j, j+checkPoint):
                            cnt[arr[a][b]] += 1 #0이랑 1 각각 몇갠지 더하기
                    if cnt[0] == 0 or cnt[1] == 0 : #압축이 가능하다!
                        
                        if cnt[1] == 0 :
                             total_cnt[0] += 1
                        else :
                             total_cnt[1] += 1
                                
                        for a in range(i,i+checkPoint):
                            for b in range(j, j+checkPoint):
                                arr_check[a][b] = True #방문 기록
                                
                
        checkPoint = checkPoint // 2           
        if arr_check == [[True] * len(arr) for _ in range(len(arr))]:
            break
            
    return total_cnt