#닉네임 중복 허용, 닉네임 변경 가능, 변경하면 이전에 나갔던 기록까지 불러와 닉네임 변경해야 함

#uid는 dict의 key, 닉네임은 value로 저장
def solution(record):
    user = {}
    methods = {"Enter":"님이 들어왔습니다.", "Leave":"님이 나갔습니다."}
    result = []
    for r in record:
        mun = r.split(" ") #[method, uid, nickname]
        if mun[0] != "Leave":
            user[mun[1]] = mun[2]
    for r in record:
        mun = r.split(" ") #[method, uid, nickname]
        if mun[0] in methods:
            result.append('{}{}'.format(user[mun[1]],methods[mun[0]]))
    return result