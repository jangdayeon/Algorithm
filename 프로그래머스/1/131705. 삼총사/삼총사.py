import itertools
def solution(number):
    answer = 0
    combi = itertools.combinations(number,3)
    for c in combi:
        if sum(c)==0:
            answer+=1
    return answer