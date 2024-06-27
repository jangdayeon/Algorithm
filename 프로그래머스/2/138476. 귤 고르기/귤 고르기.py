#counter이용하면 될 것 같다.
def solution(k, tangerine):
    tangerine_cnt = dict()
    for t in tangerine: #counter
        if t in tangerine_cnt :
            tangerine_cnt[t] += 1
        else :
            tangerine_cnt[t] = 1
    tangerine_cnt_sorted = sorted(tangerine_cnt,key=lambda x:tangerine_cnt[x]) #귤크기별 개수 정렬
    idx = 0
    k = len(tangerine)-k #빼야하는 귤 개수
    while k: 
        if tangerine_cnt[tangerine_cnt_sorted[idx]] > 0 : #귤 개수가 0보다 많을 때
            tangerine_cnt[tangerine_cnt_sorted[idx]] -= 1
            k-=1
        if tangerine_cnt[tangerine_cnt_sorted[idx]] == 0: #귤 개수가 0이면 다음 크기의 귤로 이동
            tangerine_cnt.pop(tangerine_cnt_sorted[idx])
            idx+=1
    return len(tangerine_cnt)