import sys
input= sys.stdin.readline

cost = [None] * 3
a,b,c = map(int, input().split())
big = 0
for i in range(3):
    cost[i] = list(map(int, input().split()))
    big = max(cost[i]) if big<max(cost[i]) else big
li = [0] * (big+1)
for i in range(3):
    for j in range(cost[i][0], cost[i][1]):
        li[j] +=1
print((li.count(3)*c*3)+(li.count(2)*b*2)+(li.count(1)*a))
