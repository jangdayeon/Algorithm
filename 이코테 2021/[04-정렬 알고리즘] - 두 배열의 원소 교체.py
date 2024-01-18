import sys
input = sys.stdin.readline

n, k = map(int, input().split()) #n:원소의 개수, k:몇 번 바꿔치기하는 지
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(k):
    findA = a.index(min(a))
    findB = b.index(max(b))
    a[findA] = max(b)
    b[findB] = min(a)

print(sum(a))
