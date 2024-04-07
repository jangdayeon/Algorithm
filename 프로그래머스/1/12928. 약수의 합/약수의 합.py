import math
def solution(n):
    s = math.floor(math.sqrt(n)) #제곱근 구하기
    print(s)
    answer = 0
    if n==0:
        return 0
    elif n==1:
        return 1
    for i in range(1,s+1):
        if n%i==0:
            if i == n//i:
                answer +=i
            else:
                answer += i + n//i
    return answer