#컨테이너 한 방향 진행 -> 큐 이용
#순서 맞지 않는 상자는 보조 컨테이너 벨트에 추가 -> 스택 이용
#보조에도 순서X -> 싣지X

#자료구조 빡구현 문제
#시간복잡도 유의 O(1)

from collections import deque
def solution(order):
    order_idx = 0
    first = deque([i for i in range(1,len(order)+1)])
    second = []
    result = 0
    while order_idx != len(order):
        if not first: #메인은 텅텅인데
            if second and order[order_idx] == second[-1]: #보조에는 있다?
                # print("보조에서 빼내", now)
                order_idx += 1         
                second.pop()
                result +=1
                continue
            else:
                break
        now = first[0]
        if now != order[order_idx]: #메인에 값은 있는데 순서가 틀림
            if second and order[order_idx] == second[-1]: #보조에는 있다?
                # print("보조에서 빼내", now)
                order_idx += 1         
                second.pop()
                result +=1
            else: #보조에도 없다?
                # print("보조에 추가해", now)
                second.append(now) #second에 추가
                first.popleft()
        else: #메인에 값은 있고 순서 맞아서 보낼 수 있음
            # print("바로 보낼 수 있어", now)
            first.popleft()
            order_idx += 1
            result += 1
    return result
            