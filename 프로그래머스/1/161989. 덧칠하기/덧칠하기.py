def solution(n, m, section):
    li = [True] * n
    for i in section: #벗겨진 곳 체크
        li[i-1] = False
    answer = 0
    for sec in section: 
        if li[sec-1] == False: #벗겨진 곳 찾고
            if sec-1+m >= len(li): #벗겨진 곳부터 칠하려고 하는데 벽을 넘어갈 경우
                li[sec-1:] = [True] *len(li[sec-1:])
            else: #그냥 칠하면 되는 경우
                li[sec-1:sec-1+m] = [True] * len(li[sec-1:sec-1+m])
            answer +=1 #페인트칠 몇 번 했는지 체크
    return answer  