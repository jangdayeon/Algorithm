import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

wh = [[-1,0],[1,0],[0,-1],[0,1]] #상,하,좌,우
def dfs(a,b,pan):
    pan[a][b] = 2
    for i in range(4):
        where = wh[i]
        if(a+where[0]>-1 and a+where[0]<len(pan) and b+where[1]>-1 and b+where[1]<len(pan[0])):
            if(pan[a+where[0]][b+where[1]] ==1):
                dfs(a+where[0],b+where[1],pan)
    return pan

rst = 0
T = int(input())
for _ in range(T):
    rst = 0
    m,n,k = map(int, input().split())
    pan = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a,b = map(int, input().split())
        pan[b][a]=1
    #여기까지 입력 끝
    
    for i in range(n):
        for j in range(m):
            if(pan[i][j]==1):
                pan = dfs(i,j,pan)
                rst+=1
    print(rst)