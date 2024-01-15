import sys
input = sys.stdin.readline

n = int(input())
rest =1000-n
rst =0
coin = [500,100,50,10,5,1]

for i in coin:
    rst += rest//i
    rest = rest%i
print(rst)