import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

n,m = map(int, input().split()) #전체 회사의 개수, 경로의 개수
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

x, k = map(int,input().split()) # A는 k번 회사를 거쳐 x번 회사로 가는 최소 이동 시간을 궁금해 함
def dijkstra(start, end):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        print("왜", *distance)
        if(distance[now]< dist):
            continue
        if(len(graph[now])>0):
            for i in graph[now]:
                if(distance[i]>dist+1):
                    distance[i] = dist+1
                    heapq.heappush(q, (dist+1,i))
    print(*distance)
    return distance[end]
print(*graph)
pp = dijkstra(1,k)
print(*graph)
qq = dijkstra(k,x)
print(pp+qq)