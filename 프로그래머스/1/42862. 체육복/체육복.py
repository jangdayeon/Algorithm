#한 번 틀림. lost를 오름차순으로 정렬 후 앞 친구 꺼를 최대한 빌려쓰도록 코드 작성
#두 번 틀림. 번호가 무조건 1부터 n까지라는 말이 지문에 없다.
#세 번 틀림. 본인 우선으로 빌려주도록 했는데 테케 하나가 추가로 통과되었다.. 이해하기 어려움
    #-> 답 찾아봄..하하 내가 여벌 갖고 있고 도난당하면 아무한테도 못빌려줌^^.. 이런 값은 미리 lost에서 제거해줘야 함. 

def solution(n, lost, reserve):
    lost.sort()
    lostAndHave = set(lost) & set(reserve)
    for lah in lostAndHave: #본인이 도난 당하고 여분도 갖고 있을 경우 교집합을 이용해서 제거
        lost.remove(lah)
        reserve.remove(lah)
    for i,noS in enumerate(lost):
        if noS-1 in reserve: #내 앞이 빌려줄 수 있는 경우
            lost[i] = 0
            reserve.remove(noS-1)
        elif noS+1 in reserve: # 내 뒤가 빌려줄 수 있는 경우
            lost[i] = 0
            reserve.remove(noS+1)
        else :
            lost[i] = 1
    return n - sum(lost)