#한 번 틀림. 답 확인. cacheSize가 0일 때 deque에 값을 넣는 문제가 발생함
from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5*len(cities)
    cities = map(lambda x:x.lower(), cities) #소문자로 수정
    cacheList = deque([""] * cacheSize) #캐시 담을 곳
    result = 0
    for c in cities: 
        if c in cacheList: #캐시에 저장된 값이면
            cacheList.remove(c)
            cacheList.append(c)
            result += 1
        else : #저장되지 않은 값이면
            if cacheList :
                cacheList.popleft()
            cacheList.append(c)
            result += 5
    return result
    