from collections import deque

def solution(priorities, location):
    where = location
    rtn = 1
    queue = deque(priorities)
    while len(queue)>1:
        a = queue.popleft()
        if(a >= max(queue)): #첫 번째 노드가 가장 큰 수였을 경우
            if(where ==0): #알고 싶었던 노드였을 경우
                return rtn
            else: #아닌 경우
                where -= 1
            rtn +=1
        else: #가장 큰 수가 아니였을 경우
            queue.append(a)
            if(where == 0):
                where = len(queue)-1
            else:
                where -=1
    return rtn
            