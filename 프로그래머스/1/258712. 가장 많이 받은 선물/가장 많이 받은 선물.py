# 1. 입출력 예의 첫번째 그래프처럼 먼저 나타낸다. ->g1
    # g1의 대각선은 -1,-2,-3처럼 음수의 각기 다른 수로 저장한다.
# 2. 두번째 그래프처럼 연산을 통해 저장한다. ->g2
# 3. g1을 통해 선물 받은 사람을 조회하는데 이때, [1][2]인 곳과 [2][1]인 곳을 비교해서 (1)같거나(2)더 큰 경우에는 g3에 선물 받은 수를 추가한다.
# 4. g3에서 가장 큰 수를 리턴한다.
def solution(friends, gifts):
    #1
    friendsNum = dict(zip(friends, [i for i in range(len(friends))])) #frineds 이름에 인덱스 지정
    
    g1 = [[0 for _ in range(len(friends))] for _ in range(len(friends))]

    for g in gifts:
        fr, to = g.split(" ") #준 사람, 받은 사람
        g1[friendsNum[fr]][friendsNum[to]] +=1
    
    #2
    g2 = [[0 for _ in range(3)] for _ in range(len(friends))]
    for i in range(len(friends)):
        g2[i][0] = sum(g1[i])
        g2[i][1] = sum([g1[j][i]for j in range(len(friends))])
        g2[i][2] = g2[i][0]-g2[i][1]
    
    for i in range(len(friends)):
        g1[i][i] = -i-1 #g1 기본세팅
    
    # print(g1)
    # print(g2)
    
    #여기까지 g1,g2 세팅 끝
    
    #3
    g3 = [0] * len(friends)
    for i in range(len(friends)):
        for j in range(len(friends)):
            if(g1[i][j]==g1[j][i]):
                if(g2[i][2]>g2[j][2]):
                    g3[i]+=1
            elif(g1[i][j]>g1[j][i]):
                g3[i]+=1
    #4
    return max(g3)    