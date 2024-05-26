#우선 며칠이 걸리는지 구해서 리스트에 저장
#이전보다 일자가 짧으면 이전값에 +1, 길면 비교 값 업데이트
def solution(progresses, speeds):
    for i,s in enumerate(speeds):
        pro = 100-progresses[i]
        if pro % s == 0 :
            progresses[i] = pro // s
        else :
            progresses[i] = pro // s + 1
    
    result = dict()
    maxi = 0
    for p in progresses:
        if not result or maxi < p :
            result[p] = 1
            maxi = p
        else :
            result[maxi] += 1
    return list(result.values())