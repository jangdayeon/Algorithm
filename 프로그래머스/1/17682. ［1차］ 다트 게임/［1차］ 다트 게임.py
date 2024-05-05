#bonus = dict으로 s,d,t를 1,2,3이라고 값 저장
#점수별로 계산 후 옵션은 점수별로 계산된 값에 추가 적용시키는 방법으로 진행
#dr = dartResult는 숫자를 기준으로 나눠 저장하기

#정확도에서 한 번 틀림-> 첫번째 점수가 10일 경우 예외처리 안해서
#정확도에서 또 틀림 -> 10S10S10S인 경우 list split 잘못되는 문제 발생
import re

def solution(dartResult):
    bonus = {'S':1,'D':2,'T':3}
    # dr = re.split('[0-9]',dartResult) #이렇게 정규식으로 split했더니 숫자가 지워지는 문제 발생
    dr = []
    startSplit = 0
    for i,d in enumerate(list(dartResult)): #숫자를 기준으로 문자열 나누기
        if i>1 and d.isdigit():
            dr.append(dartResult[startSplit:i])
            startSplit = i
        elif i == len(dartResult)-1:
            dr.append(dartResult[startSplit:])
    
    drIdx = len(dr)-1 #숫자가 10인 경우 1,0T로 나눠 dr에 저장되는 문제 해결하기 위한 반복문
    while drIdx>0:
        if dr[drIdx].isdigit():
            dr[drIdx+1] = dr[drIdx]+dr[drIdx+1]
            dr.pop(drIdx)
            drIdx -=2
        else:
            drIdx -=1
            
    result = [0] * 3 #dart별 계산한 값 저장
    for i in range(3):
        if dr[i].find('S')>=0:
            score, option = dr[i].split('S')
            result[i] = int(score)
            if option != '':
                if option == '#':
                    result[i] = -result[i]
                else:
                    result[i] *=2
                    if i != 0:
                        result[i-1] *=2
        elif dr[i].find('D')>=0:
            score, option = dr[i].split('D')
            result[i] = int(score)**2
            if option != '':
                if option == '#':
                    result[i] = -result[i]
                else:
                    result[i] *=2
                    if i != 0:
                        result[i-1] *=2
        else:
            score, option = dr[i].split('T')
            result[i] = int(score)**3
            if option != '':
                if option == '#':
                    result[i] = -result[i]
                else:
                    result[i] *=2
                    if i != 0:
                        result[i-1] *=2
    # print(*dr)
    # print(*result)
    return sum(result)