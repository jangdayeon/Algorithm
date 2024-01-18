#dp 문제인데.. 이 문제 답지 봤음
# n-2번에 생각했던 것이 나은가 n-1번에 생각했던 것이 나은가를 고려하는 것
#dp는 차례대로 순서를 만들어서 "점화식"을 만드는 것이 중요하다.

import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

li = [0] * 100
def dp():
    li[0] = num[0]
    li[1] = max(num[0],num[1])
    for i in range(2,n):
        li[i] = max(li[i-2]+num[i], li[i-1])
    print(li[n-1])
dp()