from itertools import combinations 

#category끼리 정렬해서 인덱스를 지정해주고, 해당 인덱스에 옷이 몇 개인지 clo에 저장해주기
def solution(clothes):
    category = list(set(list(map(lambda x:x[1], clothes))))
    category = sorted(category)
    clo = [0 for _ in range(len(category))]
    for i in clothes:
        clo[category.index(i[1])] +=1
    # print(*category)
    # print(*clo)
    
    
    ###############이렇게 조합을 구해 계산하면 시간 초과 나옴##############
    ########해결방법 옷 카테고리가 2가지일 경우 (N+1)(M+1)-1임. 한 옷을 입지 않는 경우의 수(+1)을 더하고, 모두 안 입을 경우의 수(-1)을 통해 계산 ##########################
    # forCombi = 1
    # for i in clo:
    #     forCombi *=i
    # answer = sum(clo) #한 개 고를 경우
    # #이 아랜 두 개 이상 고를 경우
    # for i in range(2,len(clo)+1): # i_C_j
    #     a = combinations(clo,i) #combinations함수로 조합을 구하고
    #     for j in a: #조합별로 수를 다 곱해 answer에 더하기
    #         b = list(j) 
    #         c = 1
    #         for k in b :
    #             c *=k
    #         answer +=c
        answer = 1
        for i in clo:
            answer *= (i+1)
    return answer-1