#접두사 합
#첫번째 틀림. 시간 초과 -> 효율 높이기 위해 start_idx 추가
#두번째 틀림. 답 찾아본 결과 L,R 인덱스를 통해 문제를 풀어야 한다는 것을 알게 됨
def solution(sequence, k):
    l = 0
    r = 1
    tmp = [0,sequence[0]]
    for i in range(1,len(sequence)):
        tmp.append(sequence[i] + tmp[i])

    result = [0,len(sequence)]
    while l < len(tmp) and r < len(tmp):
        if tmp[r]-tmp[l] < k: #부분합이 k보다 작을 경우 r 인덱스 옮기기
            r += 1
        elif tmp[r]-tmp[l] > k : #부분합이 k보다 클 경우 l 인덱스 옮기기
            l += 1
        else : #부분합이 k와 같을 경우 l 인덱스 옮기기
            if r-1-l < result[1]-result[0]:
                result = [l,r-1]
            l += 1
            
    return result
            
            