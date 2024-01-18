import sys
input = sys.stdin.readline
from bisect import bisect_left

n,m = map(int, input().split()) #칭호 수, 캐릭터들의 개수
lev = [] #레벨 단위

for i in range(n):
    lev.append(input().split())
levChk = list(map(lambda x:int(x[1]),lev))

def binary_search(a):
    idx = bisect_left(levChk,a)
    print(lev[idx][0])

for i in range(m):
    binary_search(int(input()))