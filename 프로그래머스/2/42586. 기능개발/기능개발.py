#progresses 각각 며칠 걸리는지 계산
#인덱스 전의 값이 더 크면 append 1하지말고 해당 인덱스에 1 추가하기

import math
def solution(progresses, speeds):
    answer = []
    m = 0
    for i in range(len(progresses)):
        x = math.ceil(( 100 - progresses[i] ) / speeds[i])
        if(len(answer)==0):
            answer.append(x)
        elif(answer[len(answer)-1]<x):
            answer.append(x)
        else:
            answer.append(answer[len(answer)-1])
    realAns = []
    cnt = 0
    chk = answer[0]
    for i in range(len(answer)):
        print(answer[i])
        if(answer[i]!=chk):
            realAns.append(cnt)
            cnt = 1
            chk = answer[i]
        else:
            cnt +=1
        if(i == len(answer)-1):
                realAns.append(cnt)
    return realAns