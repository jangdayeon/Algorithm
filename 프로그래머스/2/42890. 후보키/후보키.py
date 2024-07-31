#한 번 틀림. 답 확인 후 최소성이 확인된 컬럼을 지웠던 방식에서 지우지 않고, 확인을 건너뛰는 방식으로 바꿔 구현함
#두 번 틀림. 최소성은 23 /124 일 경우는 최소성이 2개이다. 즉, 2가 중복되어도 124의 부분집합이 23이 아니므로 된다! 이것을 기반으로 수정 필요
from itertools import combinations
def solution(relation):
    result = 0
    
    #행->열, 열->행으로 바꾸기 
    relation_ = [[] for _ in range(len(relation[0]))]
    relation_should_del = []
    for j in range(len(relation[0])):
        for i in range(len(relation)):
            relation_[j].append(relation[i][j])
        #속성 하나로 후보키 가능한 것 제거하기 위해 삭제할 리스트에 저장
        if len(set(relation_[j])) == len(relation_[j]):
            relation_should_del.append(j)
            result += 1
    for r in sorted(relation_should_del, reverse=True):
        relation_.pop(r)

    #속성 2개 이상으로 후보키 가능한 것 확인하기
    combi = [] #조합 저장
    for i in range(2,len(relation_)+1):
        combi.extend(combinations(range(len(relation_)), i))
    #조합한 내용으로 후보키만들 수 있느지 확인
    already = []
    for i in combi:
        for a in already: #최소성 확인
            if set(a) | set(i) == set(i): 
                break
        else:
            tmp_l = [] 
            li = list(map(lambda x:relation_[x],i))
            for j in range(len(li[0])):
                tmp = []
                for z in range(len(li)):
                    tmp.append(li[z][j])
                tmp_l.append(tuple(tmp))
            #zip 완성 후 유일성 확인
            if checkList(tmp_l):
                already.append(i)
                result += 1
    return result
        
def checkList(tmp_l):
    if len(set(tmp_l)) == len(tmp_l) :
        return True
    else:
        return False