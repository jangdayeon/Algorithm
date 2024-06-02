#우선순위 힙으로 구현
#한 번 틀림. 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우를 고려하지 않아서
import heapq
def solution(scoville, K):
    heapq.heapify(scoville) #힙으로 변환
    result = 0
    while scoville[0]<K:
        if len(scoville) < 2 :
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+(b*2))
        result +=1
    return result
    