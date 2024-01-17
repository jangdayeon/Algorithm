import sys
input = sys.stdin.readline
from collections import deque

n = int(input()) #전체 사람 수
a, b = map(int, input().split()) #a와 b 촌수 계산 후 출력해야 함
c = int(input()) #관계 수
rlt = [[] for _ in range (n+1)]
chk = [-1 for _ in range(n+1)]
for _ in range(c):
    x,y = map(int, input().split()) #부모, 자식
    rlt[x].append(y)
    rlt[y].append(x)
# 입력 끝

def bfs():
    queue = deque([a])
    chk[a] = 0
    while queue:
        v = queue.popleft()
        for i in rlt[v]:
            if (chk[i]==-1):
                queue.append(i)
                chk[i] = chk[v]+1
            
bfs()
if(chk[a] == -1 or chk[b] == -1 ):
    print(-1) #종료
else:
    print(abs(chk[a]-chk[b]))