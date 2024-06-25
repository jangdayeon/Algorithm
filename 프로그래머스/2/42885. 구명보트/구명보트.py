from collections import deque
def solution(people, limit):
    people.sort(reverse=True)
    dq = deque(people)
    answer = 0
    while dq:
        heavy = dq.popleft()
        if dq and limit >= heavy+dq[-1] :
            dq.pop()
        answer += 1
    return answer