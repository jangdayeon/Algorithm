n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
    
li = sorted(li, reverse=True)
rst = 0
for i in range(1,n+1):
    rst += li[i-1] - (i-1) if li[i-1] - (i-1) > 0 else 0 
print(rst)