import sys
input = sys.stdin.readline

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

rst = 1
for i in range(n0, 101):
    fn = a1 * i + a0
    gn = i
    if (fn>c*gn):
        rst = 0
        break

print(rst)