def solution(places):
    result = []
    for i in range(len(places)): #i번째 대기실의 j행 k열
        result.append(socialDistancing(i,places))
    return result
                            
def socialDistancing(i, places):
    manhattans_0 = [(-1,0),(0,1),(1,0),(0,-1)] # 상하좌우로 파티션 0개 확인
    manhattans_1 = [(-2,0),(0,2),(2,0),(0,-2)] # 1칸 떨어진 상하좌우로 파티션 1개 확인
    manhattans_2 = [(-1,-1),(-1,1),(1,1),(1,-1)] # 대각선으로 파티션 2개 확인
    
    for j in range(len(places[0])):
        places[i][j] = list(places[i][j])
    for j in range(len(places[0])):
        for k in range(len(places[0][0])):
            if places[i][j][k] == 'P':
                for (m_j,m_k) in manhattans_0:
                    if -1<j+m_j<5 and -1<k+m_k<5 and places[i][j+m_j][k+m_k] == 'P':
                        return 0
                for l, (m_j,m_k) in enumerate(manhattans_1):
                    if -1<j+m_j<5 and -1<k+m_k<5 and places[i][j+m_j][k+m_k] == 'P':
                        if places[i][j+manhattans_0[l][0]][k+manhattans_0[l][1]] != 'X':
                            return 0
                for (m_j,m_k) in manhattans_2:
                    if -1<j+m_j<5 and -1<k+m_k<5 and places[i][j+m_j][k+m_k] == 'P':
                        if places[i][j+m_j][k] != 'X' or places[i][j][k+m_k] != 'X':
                            return 0
    return 1
        