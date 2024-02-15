#heapq를 이용하여 [] 리스트를 넣돼, 첫번 째 값에 따라 정렬되므로, 첫번째값에 소요 시간을 넣기
#heapq에 이전 작업이 끝난 시점부터 지금 작업이 끝난 시점까지 시작할 수 있는 작업이 있는지 찾아보고, 해당 작업을 heapq에 넣기
#정렬된 값에서 작업 하나를 빼서 작업하기
#위 과정을 jobs의 길이가 0이 될때까지 지속하기

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