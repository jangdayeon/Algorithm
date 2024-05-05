#런타임 에러의 원인을 찾고자 round 함수를 사용하여 계산했지만 이것이 오히려 실패요인이 됨
#두번째 런타임 에러 해결법은.. 찾아보니 "스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의"를 안해줘서 생기는 문제였다.

def solution(N, stages):
    where = [0] * (N+1) #스테이지별 남아있는 사용자 수 초기화
    for s in stages:
        if 0 < s <= N :
            where[s]+=1
    tryMan = len(stages) #스테이지에 도달한 플레이어 수
    for i in range(1,N+1):
        temp = where[i]
        if temp == 0 : #도달한 유저가 없는 경우 실패율 0으로 정의
            where[i] = 0
        else : #도달한 유저가 있는 경우
            where[i] = temp/tryMan #실패율로 값 변경
            tryMan -= temp #다음 스테이지로 이동한 플레이어 수로 변경
    result = list(zip([i for i in range(1,N+1)], where[1:N+1])) #(스테이지,실패율)
    result.sort(key = lambda x : x[1], reverse= True) #내림차순 정렬
    return list(map(lambda x : x[0], result)) #스테이지만 출력