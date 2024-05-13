# 1. brown + yellow 한 값의 약수 짝을 구하고,
# 2. 공약수를 a와 b라고 했을 때 (a+b) * 2 - 4 == brown인지 확인하고 만약 맞다면 그대로 리턴하기
def solution(brown, yellow):
    by = brown + yellow
    checkList = []
    for i in range(1,int(by**(1/2))+1):
        if by % i == 0 :
            checkList.append((i,by//i))
    for a,b in checkList:
        if (a+b)*2-4 == brown :
            return [b,a]