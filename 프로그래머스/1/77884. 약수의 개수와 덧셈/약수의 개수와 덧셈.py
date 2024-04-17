import math

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if countDivisor(i) % 2 == 0: #약수의 개수가 짝수인지 확인
            answer +=i
        else:
            answer -=i
    return answer

def countDivisor(m):
    cnt = 0
    for i in range(1,math.floor(math.sqrt(m))+1): #효율을 위해 제곱근까지 계산하여 약수 구함
        if m != i*i:
            cnt +=2
        else:
            cnt +=1
    return cnt