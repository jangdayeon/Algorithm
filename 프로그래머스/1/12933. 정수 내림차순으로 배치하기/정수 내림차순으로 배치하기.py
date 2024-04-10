def solution(n):
    answer = ''.join(sorted(list(str(n)),reverse=True))
    return int(answer) #파이썬에서는 변수가 int의 범위를 넘어서면 자동으로 long으로 바뀐다고 함