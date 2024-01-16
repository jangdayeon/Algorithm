import sys
input = sys.stdin.readline

n,m = map(int, input().split())

pan = []
wh = [[-1,0],[1,0],[0,-1],[0,1]] #상,하,좌,우
rst=0
def bfs(i,j):
    pan[i][j]=1
    for k in range(4):
        where = wh[k]
        if(i+where[0]>-1 and i+where[0]<n and j+where[1]>-1 and j+where[1]<m):
            if(pan[i+where[0]][j+where[1]]==0):
                bfs(i+where[0],j+where[1])


for i in range(n):
    pan.append(list(map(int,list(input().strip()))))
for i in range(n):
    for j in range(len(pan[0])):
        if(pan[i][j]==0):
            bfs(i,j)
            rst+=1
print(rst)