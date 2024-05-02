#1. 먼저 최대 이익을 내기 위해서는 오름차순으로 정렬 후 사과 포장을 해야 한다.
#2. 반복문으로 사과 점수가 높은 것부터 포장을 해서 포장이 가능할 때까지 지속한다.
#3. 포장할 때마다 최대 이익을 업데이트하고, 이 값을 리턴한다.
def solution(k, m, score):
    score.sort(reverse=True) # 1.그냥 1이랑 2를 합쳐서 내림차순으로 정렬해서 사과 점수가 높은 것부터 순회할 수 있도록 할 계획
    result = 0
    for i in range(0,len(score),m):#2.
        if (i+m)<=len(score):
            result+=min(score[i:i+m])*m #3.
    return result