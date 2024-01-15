import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a = int(input())
    print('%d'%(a//25), end=' ')
    a = a - 25*(a//25) #쿼터 수
    print('%d'%(a//10), end=' ')
    a = a - 10*(a//10) #다임 수
    print('%d'%(a//5), end=' ')
    a = a - 5*(a//5) #니켈 수
    print('%d'%(a))