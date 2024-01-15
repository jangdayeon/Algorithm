import sys
input = sys.stdin.readline

a,b = map(int, input().split())

yack = []
for i in range(1,a+1):
    if(a%i==0):
        yack.append(i)
if(len(yack)<b):
    print(0)
else:
    print(yack[b-1])