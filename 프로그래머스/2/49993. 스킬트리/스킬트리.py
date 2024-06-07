#skill의 C,B,D를 skill_trees에 index를 구해 order =  []에 각 인덱스에 맞는 값을 넣고
#만약 order에 있는 값보다 index가 더 낮으면 해당 값을 지워버린다.

#첫번째 틀림. skill_trees에 해당 skill 없는 경우를 고려한다는 것을 깜빡함..
#두번째 틀림. 테케 3,5,13 틀림. 
    # -> 답 찾아봄
    # skill = "CBD"
    # skill_trees = ["CED"] 인 경우 답이 1이 나와서 생긴 문제였음..
def solution(skill, skill_trees):
    order = dict(zip(skill_trees,[ [-1,-1] for _ in range(len(skill_trees)) ] )) 
    # "BACDE" : [마지막 skill, 마지막 skill의 skill_trees에서의 위치]
    for j, s in enumerate(skill):
        where_del = []
        for i in range(len(skill_trees)):
            idx = skill_trees[i].find(s) #위치 찾고
            if idx == -1 : #skill이 없는 경우 고려
                continue
            if order[skill_trees[i]][1] == -1 and j>=1: #앞 스킬이 아예 안나왔는데 뒤 스킬 나올 경우
                print(s, skill_trees[i])
                where_del.append(i)
                continue
            if order[skill_trees[i]][1] > idx or order[skill_trees[i]][0]+1 < j : #위치가 이전 스킬보다 앞에 있다?
                where_del.append(i) #이건 불가능한 스킬트립
            else: #위치가 이전 스킬보다 뒤이다?
                order[skill_trees[i]][1] = idx #아직까진 가능하니 order 인덱스 갱신
                order[skill_trees[i]][0] = j
        where_del.sort(reverse=True) #삭제할 인덱스를 내림차순 정렬해 뒤 인덱스부터 삭제 가능하도록 함
        for w in where_del: #삭제 코드
            skill_trees.pop(w)
    return len(skill_trees)
            