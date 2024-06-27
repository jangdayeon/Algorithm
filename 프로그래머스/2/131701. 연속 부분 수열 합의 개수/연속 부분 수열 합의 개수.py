def solution(elements):
    result = set(elements)
    result.add(sum(elements))
    for i in range(2,len(elements)): #길이가 2~len(elements)까지 수열
        for j in range(len(elements)): #부분 수열 시작점
            if j+i < len(elements):
                result.add(sum(elements[j:j+i]))
            else:
                result.add(sum(elements[j:]+elements[:j+i-len(elements)]))
    return len(result)