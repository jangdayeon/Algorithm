from itertools import combinations
import math
def solution(nums):
    combi = list(map(lambda x : sum(x), combinations(nums,3)))
    #소수 판별 리스트 만들기#######################
    mc = max(combi)
    sosu = [True] * (mc+1)
    sosu[0], sosu[1] = False, False
    for i in range(2,mc+1):
        for j in range(2,math.ceil((mc+1)/i)):
            sosu[i*j]=False
    ############################################
    result = 0
    for c in combi:
        if sosu[c]:
            result +=1
    return result