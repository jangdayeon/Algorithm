import heapq
def solution(jobs):
    answer = 0
    h = []
    i,now, start = 0,0,-1 #인덱싱, 현재 시간, 건너띈 첫 시간
    while (i<len(jobs)):
        for j in jobs:
            if (start < j[0] <= now):
                heapq.heappush(h, [j[1],j[0]]) #걸리는 시간에 따라 정렬되도록
        if(len(h) > 0):
            a = heapq.heappop(h)
            start = now
            now += a[0]
            answer += now-a[1]
            i+=1
        else:
            now +=1
                
    return int(answer/ len(jobs))