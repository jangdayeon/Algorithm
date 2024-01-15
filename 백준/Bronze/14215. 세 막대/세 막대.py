import sys
input =sys.stdin.readline

a = list(map(int,input().split()))
a.sort()
if(a[0]==a[1] and a[1]==a[2] and a[2]==a[0]):
    print(sum(a))
elif(a[0]==a[1] or a[1]==a[2] or a[2]==a[0]):
    m = max(a)
    if(a.count(m)==2):
        print(sum(a))
    elif(2*min(a)<=m):
        print(2*sum(a)-1-2*m)
    else:
        print(sum(a))
else:
    m = max(a)
    if ((2*m) >= sum(a)):
        print(2*sum(a)-1-2*m)
    else:
        print(sum(a))