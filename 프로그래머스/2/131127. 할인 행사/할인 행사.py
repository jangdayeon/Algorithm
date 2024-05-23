#1. want랑 number을 zip하여 dict으로 만들고,
#2. discount를 10개씩 묶고 만약 counter을 통해 개수를 구한다음
#모든 원소가 1 <= 2 이면 result += 1을 하도록 코드를 짤 예정 
from collections import Counter
def solution(want, number, discount):
    
    # 1.
    want_dic = {}
    for i in range(len(want)):
        want_dic[want[i]] = number[i]
        
    result = 0
    # 2.
    for i in range(0, len(discount)-9):
        dc_c = Counter(discount[i:i+10])
        canIBuyAll = True
        for w in want_dic:
            if w not in dc_c or want_dic[w] > dc_c[w]:
                canIBuyAll = False
                break
        if canIBuyAll :
            result += 1
    
    return result