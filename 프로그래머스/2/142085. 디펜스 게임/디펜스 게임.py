#1. enemy[:k]를 최소힙에 넣은 것을 따로 저장하기(enemy_)
#2. enemy[idx] >enemy_[0] -> n-=pop(enemy_),  enemy_ += enemy[idx], idx += 1
    #2-1. enemy_[0] > enemy[idx] -> n-=(enemy[idx]), idx += 1
#3. 2번과정을 k=0 || idx == len(enemy)일때까지 지속
import heapq
def solution(n, k, enemy):
    if (k >= len(enemy) or sum(enemy)<=n) : return len(enemy) #2,3번 틀림. k>len(enemy)일 경우
    enemy_ = enemy[:k] 
    heapq.heapify(enemy_)
    idx = k
    while (n>=0 and idx != len(enemy)):
        # print(enemy_, enemy[idx],n)
        if enemy[idx] >enemy_[0]:
            n-=heapq.heappop(enemy_)
            heapq.heappush(enemy_, enemy[idx])
            idx += 1
        else:
            n-=(enemy[idx])
            idx+=1
    return idx-1 if n<0 else idx #1번 틀림. 반례3
            
    
    
    