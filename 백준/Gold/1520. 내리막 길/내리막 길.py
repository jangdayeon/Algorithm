import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

direction = [[-1,0],[1,0],[0,-1],[0,1]] #현재를 기준으로 상하좌우 
m,n = map(int, input().split()) #세로, 가로
graph = [[0 for _ in range(n)] for _ in range(m)] #그래프
visited = [[-1 for _ in range(n)] for _ in range(m)] #방문여부
for i in range(m):
    graph[i] = list(map(int, input().split()))

def dfs(l,r,h): #행,열,산의 높이
    if(l==m-1 and r==n-1):
        return 1
    if(visited[l][r] != -1):
        return visited[l][r]
    else:
        cnt = 0
        for i in direction:
            directL = l+i[0]
            directR = r+i[1]
            if (directL < m and directL>-1 and directR<n and directR>-1 ):
                if(graph[directL][directR]<h):
                    cnt +=dfs(directL, directR,graph[directL][directR])
        visited[l][r] = cnt
        return visited[l][r]

print(dfs(0,0,graph[0][0]))