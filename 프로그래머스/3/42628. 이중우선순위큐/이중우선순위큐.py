#I이면 삽입, D이면 최댓값과 최솟값을 삭제해야 하는데, 기본적으로 heapq를 사용하고, pop은 인덱스를 주어 삭제 함

import heapq

def solution(operations):
    answer = []
    for i in operations:
        a,b = i.split()
        if(a == "I"):
            heapq.heappush(answer, int(b))
        elif(b == "1"):
            if(len(answer)==0):continue
            answer.pop(len(answer)-1)
        else:
            if(len(answer)==0):continue
            answer.pop(0)
    if(len(answer)==0):
        return [0,0]
    else:
        return [max(answer),min(answer)]
    return answer