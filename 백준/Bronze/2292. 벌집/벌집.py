import sys
input = sys.stdin.readline

a = int(input())
# 1, 2~7, 8~19
# 1, 1+6*1, 7+6*2
# S(n) = S(n-1)+6*(n-1), S(1)=1

if(a == 1):
    print(1)
else:
    s = 1
    n = 1
    while(1):
        if(s>=a):
            print(n)
            break
        n+=1
        s = s+6*(n-1)