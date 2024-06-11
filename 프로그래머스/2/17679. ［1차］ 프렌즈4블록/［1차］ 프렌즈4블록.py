# 2X2로 다 제거할 수 있는지 확인 후 해당 인덱스 리스트에 추가
# 리스트를 확인해서 삭제할 수 있는 개수 구해서 0이 아니면 삭제 후 해당 개수만큼 result 증가
# 행별로 리스트에 몇 개의 값이 들어있는지 확인하고, 그 삭제 아이템 위의 값들 모두 그 개수만큼 + 진행
# 위 과정을 삭제할 수 있는 개수가 0이될 때까지 진행

#한 번 틀림. 삭제하는 과정이 틀림 -> 살아남은 아이템만 묶어 전체를 아래로 내보내도록 코드를 수정
def solution(m, n, board):
    check = dict(zip([i for i in range(n)], [set() for _ in range(n)])) #칼럼별로 지울 아이템 저장
    for i in range(m): #board를 리스트화
        board[i] = list(board[i])
    result = 0
    while True:
        where_check = set() #지운 아이템의 칼럼 저장
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '-1' and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    #값이 있는 곳에서 제거 가능한지 확인
                    check[j].add(i)
                    check[j+1].add(i)
                    check[j].add(i+1)
                    check[j+1].add(i+1)
                    where_check.add(j)
                    where_check.add(j+1)
        if not where_check: #확인해야하는 칼럼이 없는 경우 종료
            break
            
        for w in where_check: #칼럼별 확인 시작
            result += len(check[w])
            alive_item = []
            idx = 0
            for i in range(m):
                if i not in check[w]:
                    alive_item.append(board[i][w])
            for i in range(m):
                if i < m-len(alive_item):
                    board[i][w] = '-1'
                else:
                    board[i][w] = alive_item[idx]
                    idx +=1
            check[w] = set() #초기화
    return result
        
        