import sys
input = sys.stdin.readline

n = int(input())
sco = list(map(int, input().split()))

def cal(num):
    return num/max(sco)*100

sco = list(map(cal,sco))
rst = sum(sco)/n
print(rst)