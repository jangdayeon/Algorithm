import sys
input = sys.stdin.readline

S = input().strip()

rst = [-1 for _ in range(26)]

cnt = 0
for i in range(len(S)):
    if(rst[ord(S[i])-ord('a')]==-1):
        rst[ord(S[i])-ord('a')]=cnt
    cnt+=1
    
for i in range(len(rst)):
    print(rst[i], end=" ")