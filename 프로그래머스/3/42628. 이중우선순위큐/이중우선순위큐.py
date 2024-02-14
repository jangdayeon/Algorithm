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