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