import heapq
def solution(k, score):
    h = []
    result = []
    for s in score:
        heapq.heappush(h,s) #우선순위 큐에 값 추가
        if len(h)>k: #명예의 전당 자리수를 넘었을 경우 하나 제거
            heapq.heappop(h)
        result.append(h[0]) #발표 점수 result에 추가
    return result            