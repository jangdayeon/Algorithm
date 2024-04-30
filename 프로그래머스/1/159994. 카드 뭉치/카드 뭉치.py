def solution(cards1, cards2, goal):
    where = "cards1" #탐색할 cards 초기화
    idx1 = 0 #cards1의 인덱스
    idx2 = 0 #cards2의 인덱스
    for i,g in enumerate(goal) :
        if where =="cards1":
            if idx1>=len(cards1): #cards1 다 소진됐을 경우
                where = "cards2"
                if cards2[idx2:]==goal[i:]:
                    return "Yes"
                else:
                    return "No"
            else:
                if cards1[idx1] == g:
                    idx1+=1
                else:
                    if idx2<len(cards2): #cards2로 대신해서 탐색 가능한지 확인
                        if cards2[idx2]==g:
                            where = "cards2"
                            idx2+=1
                        else:
                            return "No"
                    else:
                        return "No"                 
        elif where =="cards2":
            print(g)
            if idx2>=len(cards2): #cards2 다 소진됐을 경우
                where = "cards1"
                if cards1[idx1:]==goal[i:]:
                    return "Yes"
                else:
                    return "No"
            else:
                if cards2[idx2] == g:
                    idx2+=1
                else:
                    if idx1<len(cards1): #cards1로 대신해서 탐색 가능한지 확인
                        if cards1[idx1]==g:
                            where = "cards1"
                            idx1+=1
                        else:
                            return "No"
                    else:
                        return "No"    
    return "Yes"     