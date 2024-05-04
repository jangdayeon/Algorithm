#첫 시도 : itertools.product(canSpeak,repeat=15) 쓰려고 했으나 시간초과로 안됨
#두번째 시도 : 발음할 수 있는 것을 단어 수 만큼 지워 가며 전체 발음 가능한지 확인
#세번째 시도 : "반복"해서만 발음을 못한다는 것이었음.. 그런데도 실패..? 실수,,ㅎ

import itertools
def solution(babbling):
    result = 0
    cs2 = ["ye", "ma"] #초기화
    cs3 = ["aya","woo"] #초기화
    for i in range(len(babbling)):
        while True:
            if len(babbling[i]) == 0:
                result +=1
                break
            elif babbling[i][0:2] in cs2 :
                if babbling[i][2:4] == babbling[i][0:2]:
                    break
                babbling[i] = babbling[i][2:]
            elif babbling[i][0:3] in cs3 :
                if babbling[i][3:6] == babbling[i][0:3]:
                    break
                babbling[i] = babbling[i][3:]
            else:
                break
    return result