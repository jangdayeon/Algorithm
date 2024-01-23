a = list(input().strip())
rst = [0] * 26
for i in a:
    rst[ord(i)-ord('a')] += 1
print(*rst)