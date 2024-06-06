#dp 문제인 것 같다 이전값의 최대값을 현재값에 더해주는 것을 끝까지 반복했다.
def solution(land):
    for i in range(1, len(land)):
        land[i][0] += max(land[i-1][1],land[i-1][2],land[i-1][3])
        land[i][1] += max(land[i-1][0],land[i-1][2],land[i-1][3])
        land[i][2] += max(land[i-1][1],land[i-1][0],land[i-1][3])
        land[i][3] += max(land[i-1][1],land[i-1][2],land[i-1][0])
    return max(land[len(land)-1])
        