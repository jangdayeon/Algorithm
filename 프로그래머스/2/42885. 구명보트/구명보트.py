#첫번째 틀림. frontIdx를 주어 앞에서부터 접근하도록 만든 것을 pop(0)으로 변경하여 해결
#두번째 틀림. 효율성에서 하나 시간 초과 발생. deque 사용 -> double linked list이기 때문에 앞뒤 값 제거가 O(1)이기 때문! list는 pop(index)일 경우 O(n)의 시간 발생!
from collections import deque

def solution(people, limit):
    people.sort() #오름차순 정렬
    d = deque(people)
    answer = 0
    while True:
        if len(d) == 0: #짝을 다 짓고 0명이 되었을 때 그대로 리턴
            return answer
        if len(d) == 1: #짝을 다 지었는데 1명 남았을 때 그 1명까지 보트 태워 리턴
            return answer+1
        b = d.pop()
        if d[0]+b <= limit:
            d.popleft()
        answer +=1
        
            