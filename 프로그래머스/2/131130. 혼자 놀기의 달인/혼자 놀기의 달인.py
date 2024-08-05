#최고 점수를 찾아야 하므로, 시작점을 i로 전부 탐색하며 그래프 사이클을 찾아야 한다.
#그래프 사이클은 서로소 구할 때 쓰는 알고리즘을 사용한다.(부모 비교)
def solution(cards):
    answer = []
    for i in range(len(cards)):
        tmp = 0
        while cards[i]: #사이클 생길 때까지
            next_i = cards[i] - 1
            cards[i], i = 0, next_i #방문한 곳은 0으로 표시하고 다음 i를 확인하기 위해 i 갱신
            tmp += 1
        answer.append(tmp)
    answer.sort()
    return answer[-1] * answer[-2]