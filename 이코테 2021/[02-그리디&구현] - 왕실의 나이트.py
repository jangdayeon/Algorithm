import sys
input = sys.stdin.readline

a = list(input().strip())
a[0] = ord(a[0])-ord('a')
a[1] = int(a[1])-1
a.reverse()
rst =0

how = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]
for i in how:
    if(a[0]+i[0]>=8 or a[0]+i[0]<0 or a[1]+i[1]>=8 or a[1]+i[1]<0):
        continue
    else:
        rst+=1
print(rst)