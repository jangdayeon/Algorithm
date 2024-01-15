import sys
input = sys.stdin.readline

# 3(2+1) 5(3+2) 9(5+4)
# a(n) = a(n-1)+(a(n-1)-1), a(1)=3
n = int(input())
if(n==1) :
    print(3*3)
else :
    a = 3
    for i in range(n-1):
        a = a + (a-1)
    print(a*a)