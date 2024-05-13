#옛날에 이코테에서 바닥공사 문제랑 비슷함
#dp로 풀어야할 듯

#첫번째 틀림. for문을 돌리는데 min2Jump값이 변경되도록 코드를 짯음;
import math
def solution(num):
    can2 = num//2
    answer = 0
    for i in range(can2+1):
        nowLen = num-i
        answer += math.factorial(nowLen)//(math.factorial(i)*math.factorial(nowLen-i))
    return answer%1234567