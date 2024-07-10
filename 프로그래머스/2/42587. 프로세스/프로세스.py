from collections import deque
def solution(priorities, location):
    for i in range(len(priorities)):
        priorities[i] = (priorities[i],i) #(우선순위, 위치)
    q = deque(priorities)
    result = 0
    while q:
        now_p, now_w = q.popleft()
        print(now_p,now_w)
        for i, (priority, _) in enumerate(q): 
            if priority > now_p : #큐에 우선순위가 더 높은 프로세스가 있다면
                q.append((now_p,now_w))
                break
            if i == len(q)-1: #큐에 우선순위가 더 높은 프로세스가 없다면
                result += 1
                if now_w == location : #찾고자하는 값과 같을 경우
                    return result
                
    return result+1
            