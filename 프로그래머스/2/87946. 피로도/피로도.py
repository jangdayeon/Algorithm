#첫 번째 아이디어
#모든 순서 경우의 수를 구하고, -> PERMUTATION LIB이용
#해당 순서가 저장된 배열을 WHILE문을 돌리고
#던전에서 활동하는 FOR문 돌리고
#던전 몇 개 갈 수 있는지 최대값을 계속 구해서 리턴하기

from itertools import permutations
def solution(k, dungeons):
    order = list(map(list,permutations(range(len(dungeons)),len(dungeons))))
    answer = -1
    for i in order: #i = [0,1,2],[0,2,1] 이런 인덱스 순서
        first = k
        count = 0
        for r,j in enumerate(i):
            if(dungeons[j][0]>first):
                answer = max(answer,count)
                break
            else:
                first = first - dungeons[j][1]
                count +=1
            if(r == len(i)-1):
                return len(i)
    return answer