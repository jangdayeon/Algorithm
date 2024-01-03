import sys
input = sys.stdin.readline

n = int(input())

cnt = 1
for i in range(1,n+1):
    print(" "*(n-i), end='')
    print("*"*cnt)
    cnt+=2
cnt-=2
for i in range(1,n):
    print(" "*(i), end='')
    cnt-=2
    print("*"*cnt)