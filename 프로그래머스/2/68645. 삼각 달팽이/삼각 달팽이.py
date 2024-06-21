def solution(n): 
    answer = [0] * (n*(1+n)//2)
    under_start = 0 #0,4,12,24
    under_next_start = 4 #4,8,12
    under_next = 1
    going_top = n # -5,-4
    going_top_start = n
    snail = 1
    now = 0
    while under_start < len(answer) and answer[under_start] == 0:
        now = under_start
        tmp = under_next
        while now < len(answer) and answer[now] == 0: #내려가기
            answer[now] = snail
            now += under_next
            snail += 1
            under_next += 1
        now = now-under_next+1
        under_next = tmp + 2
        under_start += under_next_start
        under_next_start += 4
        while now + 1 < len(answer) and answer[now+1] == 0 : #우로 가기
            answer[now+1] = snail
            now += 1
            snail += 1
        while now-going_top >= 0 and answer[now-going_top] == 0: #올라가기
            answer[now-going_top] = snail
            now -= going_top
            going_top -= 1
            snail += 1
        going_top_start -= 1
        going_top = going_top_start

    return answer 
            