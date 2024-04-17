# 구현문제
# 1. 마지막 공격 시간까지를 for문에 담고
# 2. 이 for문 내에서 gauge= [현재 체력, 연속 성공]을 업데이트하고
# if문으로 조건 별로 업데이트 진행
# 2-0. 공격 받았을 경우 gauge[0]-=attacks[1] 하고 연속 성공=0, gauge[0] <=0 일 경우에는 -1 return
# 2-2. gauge[1] == bandage[0] 일 경우, gauge[0]+=bandage[2]+bandage[1]하고 gauge[1]=0
# 2-3. else 현재 체력 +=bandage[1]
# 3. for문을 빠져나오면 현재 체력을 return

def solution(bandage, health, attacks):
    gauge = [health, 0]
    idx = 0
    #1
    for i in range(1,attacks[-1][0]+1):
        if attacks[idx][0]==i: #2-0
            gauge[0]-=attacks[idx][1]
            gauge[1]=0
            idx +=1
            if gauge[0]<=0:
                return -1
        elif(gauge[1]+1>=bandage[0]): #2-1
            gauge[0]=updateHealth(gauge[0],bandage[2]+bandage[1],health)
            gauge[1]=0
        else: #2-3
            gauge[0]=updateHealth(gauge[0],bandage[1],health)
            gauge[1]+=1
        # print(i, gauge)
    return gauge[0] #3

def updateHealth(nowH, plus, maxH):
    if nowH+plus >= maxH:
        return maxH
    else:
        return nowH+plus
            
            
            