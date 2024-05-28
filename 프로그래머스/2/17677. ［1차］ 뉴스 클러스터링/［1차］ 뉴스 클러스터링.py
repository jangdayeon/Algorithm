#한 번 틀림. 합집합을 구할 때 str1이 중복된 값이 더 많을 경우를 고려하지 못함!
#두 번 틀림. (답 확인함) return 할 때 intersection과 union 모두 0일 경우에만, 65536을 리턴해야 함!

from collections import Counter

def solution(str1, str2):
    # 1. 소문자로 변환
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 2. 문자 두 글자씩 나눠 리스트에 각각 저장, 이 때 영문자만 넣어지도록 조건을 걸음
    str1_divided = []
    str2_divided = []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            str1_divided.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            str2_divided.append(str2[i:i+2])

    # 3. set()을 통해 교집합과 합집합을 구하면,, 중복이 제거되기 때문에 직접 합,차집합 구해야 함
    # Counter을 통해 구하고자 함
    s1 = Counter(str1_divided)
    s2 = Counter(str2_divided)
    intersection = 0 #교집합
    union = len(str2_divided) #합집합
    for s in s1:
        if s not in s2:
            union += s1[s]
        else:
            if s1[s] > s2[s]: #코드 추가(틀림1)
                union += s1[s]-s2[s]
            intersection += min(s1[s], s2[s])
    
    if intersection == 0 and union == 0 :
        return 65536
    elif intersection == 0 :
        return 0
    else:
        return int((intersection/union) * 65536)