#최단 경로 알고리즘을 사용하면 된다.(다익스트라 알고리즘)
import heapq
INF = int(1e9)
def solution(N, road, K):
    distance = [INF] * (N+1)
    graph = [[] for _ in range(N+1)]
    for r in road:
        a,b,d = r[0],r[1],r[2]
        graph[a].append((b,d)) #a에서 b까지 가는데 d 거리
        graph[b].append((a,d)) #b에서 a까지 가는데 d 거리
    q = []
    heapq.heappush(q,(0,1)) #(1까지의 거리, 시작위치 1)
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now] : #현재 값이 최단경로일 경우에는 무시
            continue
        for (wh, d) in graph[now]:
            if distance[wh] > distance[now]+d:
                distance[wh] = distance[now]+d
                heapq.heappush(q,(distance[now]+d,wh))
    result = 0
    for d in distance:
        if d <= K:
            result +=1
    return result
    