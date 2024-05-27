#소모 피로도가 작은 순으로 정렬해서 하려고 했지만,, 예외 발생 가능성 있어 완전 탐색해야 함

from itertools import permutations
def solution(k, dungeons):
    permu = permutations(range(0,len(dungeons)))
    result = 0
    for p in permu:
        now_tired = k
        if result == len(dungeons): #다 탐색 가능한 경우를 찾을 경우 탐색 종료하여 효율성 높임
            break
        for i, pp in enumerate(p): #탐색
            if now_tired < dungeons[pp][0] :
                break
            else :
                now_tired -= dungeons[pp][1]
                result = max(result, i+1)
    return result
                