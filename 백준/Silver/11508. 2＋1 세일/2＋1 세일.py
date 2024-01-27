n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
li = sorted(li, reverse=True)
rst = 0

for i in range(2,n,3):
        rst += li[i-2]+li[i-1]
if(n%3!=0):
    if(n-(n//3)*3==2):
        rst += li[n-1] + li[n-2]
    else :
         rst += li[n-1]
print(rst)