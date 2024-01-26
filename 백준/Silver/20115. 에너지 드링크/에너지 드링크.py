n = int(input())
a = list(map(int, input().split()))
rst = max(a)
a.remove(rst)
rst += sum(a)/2
print(rst)
