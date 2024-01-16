import sys
from functools import reduce
input = sys.stdin.readline

town = int(input())
townToTown = list(map(int, input().split()))
price = list(map(int, input().split()))
price = price[0:len(price)-1] #도착지의 주유 가격 제거

total = 0 # result
while True:
    if(len(townToTown)==0):
        break
    if(len(townToTown)==1):
        total+=townToTown[0]*price[0]
        break
#제일 싼 주유값에서 도착지까지는 제일 싼 가격으로 쭉가기
    where = price.index(min(price))
    leng = reduce(lambda x,y:x+y, townToTown[where::])
    total += min(price)*(leng)
    townToTown = townToTown[:where:]
    price=price[:where:]
print(total)