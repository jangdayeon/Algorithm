from bisect import bisect_left,bisect_right
def solution(citations):
    citations.sort()
    answer = -1
    if(max(citations)==0):
        return 0
    for i in range(max(citations)):
        if(i>len(citations)):
            break
        where = bisect_left(citations,i)
        print(where)
        if(i <= len(citations[where::]) and i >= len(citations[:where:])):
            answer = i
    return answer