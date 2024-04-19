# 1. h,w의 상하좌우 값 중 탐색 가능한 곳의 인덱스를 search에 담고
# 2. 탐색 후 [h,w]가 search의 값들과 값이 같을 경우 answer+=1
# 3. return answer

def solution(board, h, w):
    # 1.
    search = []
    if h>0: #상
        search.append([h-1,w])
    if h<len(board)-1: #하
        search.append([h+1,w])
    if w>0: #좌
        search.append([h,w-1])
    if w<len(board[0])-1: #우
        search.append([h,w+1])
    
    # 2.
    answer = 0
    for s in search:
        if (board[s[0]][s[1]]== board[h][w]):
            answer +=1
    
    # 3. 
    return answer