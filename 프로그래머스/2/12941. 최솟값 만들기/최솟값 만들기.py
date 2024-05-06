def solution(A,B):
    A.sort(reverse=True) #작은수와 큰수가 곱해지기 위해 하나는 오름차순 하나는 내림차순으로 정렬
    B.sort()
    result = 0
    for a,b in zip(A,B):
        result += a*b #곱한 값 누적해서 더한다음 리턴
    return result