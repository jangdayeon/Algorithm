#첫번째 아이디어 : 수확한 귤의 크기별 개수를 t_count에 저장 후 오름차순 정렬을 하여 개수가 적은 것부터 상자에서 빼주다가, 만약 귤의 개수가 k개 미만이 되면 그만 빼주고 리턴하도록 함
#틀려서 정답 확인. 빼주지말고 반대로 for문을 구해 더해주는 방식으로! 구해보기
from collections import Counter
def solution(k, tangerine):
    t_count = Counter(tangerine)
    total = 0
    kinds = 0
    t_count_keys = sorted(t_count, key = lambda x:t_count[x])
    for t in t_count_keys[::-1]:
        total += t_count[t]
        kinds += 1
        if total >= k :
            return kinds
    return -1