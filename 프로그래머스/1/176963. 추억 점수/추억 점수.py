#데이터를 그대로 이용하기엔 O(n^4)정도가 나와서 dict를 이용할 것임

def solution(name, yearning, photo):
    missWho = dict(zip(name,yearning))
    answer = [0]*len(photo)
    idx = 0
    for people in photo:
        for person in people:
            if person in missWho:
                answer[idx]+=missWho[person]
        idx+=1
    return answer