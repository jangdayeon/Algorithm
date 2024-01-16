import sys
input = sys.stdin.readline

n,m=map(int, input().split()) #n=스크린 m=바구나
j = int(input())
bucket = [1,m]
rst =0
for i in range(j):
    a = int(input())
    if(a<bucket[0] or a>bucket[1]) : #바구니가 이동해야하는 경우만
        how = (a-bucket[0]) if abs(a-bucket[0])<abs(a-bucket[1]) else (a-bucket[1])
        bucket = [bucket[0]+how,bucket[1]+how]
        rst+= abs(how)
print(rst)