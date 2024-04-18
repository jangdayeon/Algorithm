def solution(price, money, count):
    need = 0
    for i in range(count+1):
        need += price*i
    return need-money if need>=money else 0