n = int(input())
solider = list(map(int, input().split()))
lis = [1 for _ in range(n)]
for i in range(1,len(solider)):
    x = solider[i]
    for j in range(0,i):
        if(solider[j]>x):
            lis[i] = max(lis[i],lis[j]+1)
print(len(solider)-max(lis))