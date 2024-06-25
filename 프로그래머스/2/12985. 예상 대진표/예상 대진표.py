# 8,4,6 -> 3 인 것에서 예외 발생
#다르게 풀어야 함

def solution(n,a,b):
    mini, maxi = (b,a) if a> b else (a,b)
    answer = 1
    while True:
        mini = mini//2 if mini%2==0 else (mini+1)//2
        maxi = maxi//2 if maxi%2==0 else (maxi+1)//2
        if mini == maxi :
            return answer
        answer+=1
    return answer
    