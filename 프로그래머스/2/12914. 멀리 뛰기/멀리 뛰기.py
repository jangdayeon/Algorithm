#dp를 이용한 답 찾아봄
def solution(n):
    if n < 3 :
        return n
    li = [0] * (n+1)
    li[1] = 1
    li[2] = 2
    for i in range(3,n+1):
        li[i] = li[i-2]+li[i-1]
        # (li[i-2] == li[i-2]에 2만큼 더 간 경우의 합)
        # (li[i-1] == li[i-1]에 1만큼 더 간 경우의 합)
    return li[n]%1234567