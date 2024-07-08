from itertools import permutations
def solution(k, dungeons):
    combi = permutations(range(len(dungeons)))
    result = 0
    for c in combi:
        now = k
        for i,cc in enumerate(c):
            least, lose = dungeons[cc][0], dungeons[cc][1]
            if now >= least:
                now -= lose
                result = i+1 if i+1>result else result
            else:
                break
    return result