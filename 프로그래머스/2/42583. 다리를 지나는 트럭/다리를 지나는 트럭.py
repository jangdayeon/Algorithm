from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    i = 0
    bridge_weight = 0
    while bridge:
        i+=1
        bridge_weight -= bridge.popleft() #삭제를 먼저했어야 함. 삭제를 추가뒤에 했더니 계속 틀렸음
        if truck_weights :
            if (bridge_weight + truck_weights[0]) <= weight:
                addTruck = truck_weights.pop(0)
                bridge.append(addTruck)
                bridge_weight += addTruck
            else :
                bridge.append(0) #이걸 수정함
    return i