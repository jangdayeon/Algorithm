#5개가 최대
#더 사용할 곡괭이가 없거나 광산에 있는 모든 광물을 캘 때까지 과정을 반복
#minerals를 5개씩 잘라서 counter한다음에 (dia 개수,iron 개수, stone 개수)로 정렬하고, 곡갱이도 dia->iron->stone 순으로 소비
from collections import Counter
def solution(picks, minerals):
    
    #미네랄 5개씩 끊어서 갯수를 저장한 것을 mineral_counter에 저장
    mineral_counter = []
    mineral_position = {'diamond':0,"iron":1,"stone":2}
    for i in range(5,len(minerals)+1,5):
        tmp = [0,0,0]
        for j in range(i-5,i):
            tmp[mineral_position[minerals[j]]] += 1
        mineral_counter.append(tmp)
        
    if len(minerals)//5*5 != len(minerals) : #5개씩 나누고 남은 것도 추가
        tmp = [0,0,0]
        for j in range(len(minerals)//5*5,len(minerals)):
            tmp[mineral_position[minerals[j]]] += 1
        mineral_counter.append(tmp)
    
    #정렬된 데이터의 index를 통해 picks에서 어떤 것을 선택해야하는지 which에 그 인덱스를 저장
    m_sort = sorted(mineral_counter, reverse=True) #  (dia 개수,iron 개수, stone 개수)로 정렬
    tired = [[1,1,1],[5,1,1],[25,5,1]] #피로도
    answer = 0
    while sum(picks) > 0 and mineral_counter:
        # print(mineral_counter)
        popOne = mineral_counter.pop(0)
        
        priority = m_sort.index(popOne)
        m_sort.pop(priority)
        which = -1
        if priority+1 <= picks[0] and picks[0]>0:#2번 틀림. priority가 인덱스라서 갯수로서는 +1해줘야함
            which = 0
        elif priority+1 <= picks[0]+picks[1] and picks[1]>0: #3번 틀림. picks[0]+picks[1]로 수정
            which = 1
        elif picks[2]>0:
            which = 2 #4번 틀림. 후순위인 건데 picks[2]==0이어서 안될 경우
        else:
            for i in [2,1,0]:
                if picks[i]>0:
                    which=i
        # print(priority, which)
            
        answer += sum(map(lambda x:x[0]*x[1],zip(tired[which],popOne)))
        picks[which] -= 1
        
    return answer
    