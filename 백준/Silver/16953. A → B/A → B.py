import sys
input = sys.stdin.readline

a,b = map(int,input().split())
cnt = 0
while(b>a):
    if(str(b)[len(str(b))-1]!='1'):
        if(b %2 != 0):
            break
        else :
            b /= 2
            b = int(b)
            cnt+=1
    else:
        b = int(str(b)[:len(str(b))-1:])
        cnt+=1
print(cnt+1 if b==a else -1)