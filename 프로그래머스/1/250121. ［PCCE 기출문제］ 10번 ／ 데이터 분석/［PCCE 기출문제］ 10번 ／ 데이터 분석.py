# 1. ext와 sort_by는 "code", "date", "maximum", "remain" 이므로 이것에 해당하는 인덱스 값 지정하기 위한 byWhat 변수 생성
# 2. ext로 기준을 확인하고 해당 인덱스의 값들을 기준으로 오름차순으로 정렬 후, val_ext 가 어디에 들어가야 하는지 bisect_right를 통해 확인 후 기준에 맞지 않는 데이터 삭제
# 3. sort_by로 기준 확인 후 해당 인덱스의 값들을 기준으로 오름차순으로 정렬 후 return
from bisect import bisect_right

def solution(data, ext, val_ext, sort_by):
    # 1.
    byWhat = {"code":0,"date":1,"maximum":2,"remain":3}
    
    # 2.
    data.sort(key= lambda x:x[byWhat[ext]])
    data = data[:bisect_right(list(map(lambda x:x[byWhat[ext]], data)), val_ext)]
    
    # 3.
    data.sort(key= lambda x:x[byWhat[sort_by]])
    return data