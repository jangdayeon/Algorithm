#최소공배수까지 *1 or *2 or *3 or *4인 조합을 찾으면 된다
#한 번 틀림. combi로 for문을 돌리면 4,999,950,000..
#dict으로 시간복잡도를 줄여보자
#두 번 틀림. combinations을 정렬하고 counter에 저장해보자
#세 번 틀림. counter을 weights에 먼저 적용하고 시소 거리가 경우의 수가 6가지라 gcd를 사용하지 말고 하드코딩
from itertools import combinations
from math import gcd
from collections import Counter
def solution(weights):
    weights_counter = Counter(weights)
    combi = combinations(weights_counter,2)
    result = 0
    
    # 무게가 다를 경우
    for (a,b) in combi: # 2-3 , 2-4 , 3-4, 3-2 , 4-2 , 4-3
        if (a*2==b*3 or a*2==b*4 or a*3==b*4 or a*3==b*2 or a*4==b*2 or a*4==b*3) :
            result += weights_counter[a]*weights_counter[b]
            
    #무게가 같을 경우
    for weight in weights_counter:
        if weights_counter[weight] > 1 :
            result += weights_counter[weight]*(weights_counter[weight]-1)//2
    
    return result
    
