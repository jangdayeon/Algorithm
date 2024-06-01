#경우를 다 구한다음 sort함수 이용

from itertools import product
def solution(word):
    mo = ['A','E','I','O','U']
    per2 = map(lambda x:''.join(x), product(mo, repeat = 2))
    per3 = map(lambda x:''.join(x), product(mo, repeat = 3))
    per4 = map(lambda x:''.join(x), product(mo, repeat = 4))
    per5 = map(lambda x:''.join(x), product(mo, repeat = 5))
    mo += per2
    mo += per3
    mo += per4
    mo += per5
    mo.sort()
    for i,m in enumerate(mo):
        if m == word :
            return i+1
    return -1