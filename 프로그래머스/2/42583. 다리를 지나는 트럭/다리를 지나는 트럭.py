#아이디어 바로 생각이 안났으니 한 번 더!

#bridge의 길이가 0이 될 때까지 while문을 돌려두고
#기본적으로, 다리를 건너는 트럭에서 하나의 값을 pop하기
#그 다음에는,,
#다음 들어올 차가 더해진 무게와 길이가 괜찮으면 대기 트럭에서 빼오고,
#안 괜찮으면 0을 추가하기

from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]* bridge_length)
    answer = 0
    current_sum = 0
    while (len(bridge)!= 0):
        # print(*bridge)
        a = bridge.popleft()
        answer +=1
        current_sum -=a
        if(len(truck_weights)!=0):
            if(current_sum+truck_weights[0]>weight):
                bridge.append(0)
            else:
                b = truck_weights.pop(0)
                bridge.append(b)
                current_sum +=b
                
    return answer