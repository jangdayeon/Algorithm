from collections import Counter

def solution(want, number, discount):
    want_cnt = sum(number)
    want_cntr = dict(zip(want,number))
    result = 0
    for i in range(want_cnt-1,len(discount)):
        cntr = Counter(discount[i-want_cnt+1:i+1])
        cntr.subtract(want_cntr)
        canBuy = True
        for _cntr in cntr:
            if cntr[_cntr] < 0 :
                canBuy = False
                break
        if canBuy:
            result +=1
    return result
                