from collections import deque 

def solution(priorities, location):
    queue = deque(list(zip([i for i in range(0,len(priorities)+1)], priorities)))
    
    result = []
    while queue: #로직 시작
        popOne = queue.popleft()
        if not queue: #마지막 원소일 경우 예외 처리
            result.append(popOne)
            break
        others = max(map(lambda x:x[1], queue)) #우선순위가 더 높은 원소가 있는지 확인
        if popOne[1] >= others :
            result.append(popOne)
        else:
            queue.append(popOne)
    
    for i,r in enumerate(result): #언제 실행된 프로세스인지 확인
        if r[0] == location :
            return i+1