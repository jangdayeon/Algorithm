n,k = map(int, input().split())

x = [1] *(n+1)
for i in range(2,n+1):
    x[i] = (x[i-1]*i)
print((x[n] // (x[k]*x[n-k]))%10007)