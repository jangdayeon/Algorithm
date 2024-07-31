#1차 방정식으로 문제 풀이 / y = a*x + b
#a를 구하고, 1~W까지 result -=ceil(a*n+b-a*(n-1)+b)
#1번 틀림. w == h인 경우는 예외처리 진행하고, 분모씩 반복되니깐, (테케1의 경우는 x=2씩 반복) 그 점을 이용해 시간 초과를 해결하고자 했다.
#2번 틀림. fractions이 비싼 함수인가보다.. gcd로 바꿨다.
#3번 틀림. 답을 확인하니 math.ceil을 통해 문제를 풀면 안되나보다..
    #아래처럼 규칙이 12,8에서 부분 사각형인 3,2에서 겹치는 사각형의 수가 다음과 같다.
    #(w' - 1) + (h' - 1) + 1 = w' + h' - 1
import math

def solution(w, h):
    # 대각선이 지나가는 정사각형의 개수는 w + h - gcd(w, h)
    gcd_value = math.gcd(w, h)
    return w * h - (w + h - gcd_value)
