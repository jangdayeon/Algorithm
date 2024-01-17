import sys
input = sys.stdin.readline
from collections import deque

def bfs(l,a,b):
    pan = [[-1 for _ in range(l)] for _ in range(l)]
    pan[a[0]][a[1]] = 0
    queue = deque([a])
    while queue:
        v = queue.popleft()
        where = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]
        for i in range(len(where)):
            where[i][0] += v[0]
            where[i][1] += v[1]
        for i in where:
            if(i[0]>-1 and i[0]<l and i[1]>-1 and i[1]<l):
                if(pan[i[0]][i[1]]==-1):
                    pan[i[0]][i[1]]= pan[v[0]][v[1]]+1
                    queue.append(i)
    return (pan[b[0]][b[1]])
                
T = int(input())
for i in range(T):
    l = int(input()) #체스판의 한 변의 길이
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    print(bfs(l,a,b))