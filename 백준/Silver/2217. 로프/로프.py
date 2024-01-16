import sys
input =sys.stdin.readline

n = int(input()) #로프의 개수
rop =[] #각 로프가 버틸 수 있는 최대 중량
for _ in range(n):
    rop.append(int(input()))
rop = sorted(rop)
m = 0
for i in range(n):
    m = rop[i]*(n-i) if m<rop[i]*(n-i) else m
print(m)