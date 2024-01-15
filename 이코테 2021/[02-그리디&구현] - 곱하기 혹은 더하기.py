import sys
input = sys.stdin.readline

s = list(map(int, list(input().strip())))

rst = s[0]
for i in range(1,len(s)):
    if(s[i]<=0 or rst<=0):
        rst+=s[i]
    else:
        rst*=s[i]
print(rst)