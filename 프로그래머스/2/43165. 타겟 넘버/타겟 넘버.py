#완전 탐색으로 문제를 풀려고 함
from itertools import product
def solution(numbers, target):
    answer = 0
    a = product(['+','-'],repeat = len(numbers))
    for aa in a:
        result = 0
        for i in zip(aa,numbers):
            if i[0] == '+':
                result += i[1]
            else :
                result -= i[1]
        if result == target :
            answer += 1
    return answer