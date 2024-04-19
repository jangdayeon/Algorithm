# 첫번째 풀이
# 1. list를 이용하여 players 이름에 해당하는 등수를 record에 저장하기
# 2. for문 내에서 index() 함수를 이용하여 callings된 사람 찾아 record 업데이트 시키기
# 3. return record

# 두번째 풀이
# record를 dict으로 만들어서 순서를 입력하도록 하고, players를 업데이트 하여 record.index() 함수를 제거한다.
def solution(players, callings):
    # 1.
    record = dict(zip(players, [i for i in range(len(players))]))
    # 2.
    for name in callings:
        location = record[name]
        p1,p2 = players[location-1],players[location]
        record[p1], record[p2] = record[p2], record[p1] #순위 업데이트
        players[location-1],players[location] = p2,p1 #이름순 업데이트
    # 3.
    return players