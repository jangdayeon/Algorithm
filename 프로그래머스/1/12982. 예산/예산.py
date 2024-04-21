def solution(d, budget):
    answer = 0
    d.sort()
    for m in d:
        if(budget>=m):
            budget-=m
            answer+=1
        else:
            break
    return answer