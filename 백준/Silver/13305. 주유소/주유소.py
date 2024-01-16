import sys
from functools import reduce
input = sys.stdin.readline

town = int(input())
townToTown = list(map(int, input().split()))
price = list(map(int, input().split()))
price = price[0:len(price)-1] #도착지의 주유 가격 제거

total = townToTown[0]*price[0] # result
m = price[0]
for i in range(1, len(townToTown)):
    if(price[i]<m):
        m = price[i]
    total += townToTown[i]*m
print(total)