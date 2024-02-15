#heapq를 이용하여 k를 넘을 때까지 2개씩 팝해서 스코빌 지수를 계산해서 push하기

import heapq


def checkK(h, K):
    for i in h:
        if(i<K):
            return False
    return True

def solution(scoville, K):
    h = []
    answer = 0
    for i in scoville:
        heapq.heappush(h, i)
    # print(*h)
    while (not checkK(h, K)):
        if(len(h)<=1):
            return -1
        first = heapq.heappop(h)
        second = heapq.heappop(h)
        heapq.heappush(h, (first+second*2))
        answer +=1
    return answer