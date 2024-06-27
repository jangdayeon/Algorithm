import math
def solution(n, words):
    turn = 0
    done = set()
    done.add(words[0])
    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0] or (words[i] in done):
            return [(i+1)%n if (i+1)%n !=0 else n, math.ceil((i+1)/n)]
        done.add(words[i])
    return [0,0]