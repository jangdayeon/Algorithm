def solution(skill, skill_trees):
    answer=0
    for st in skill_trees: # st = "BACDE"
        before, flag = 0, 0
        for s in skill :
            tmp = st.find(s)
            
            if tmp >= 0 : #st에 skill이 있을 경우
                if before == -1 : #전 스킬이 없었음! 다음 스킬도 못함
                    flag = 1
                    break
                if tmp >= before : #현재스킬이 전 스킬보다 뒤 -> 유효
                    before = tmp
                else : #현새스킬이 전 스킬보다 앞 -> X
                    flag = 1
                    break
            else: #st에 skill에 없음
                before = tmp
        if flag: 
            continue
        
        answer+=1
    return answer
        