n = int(input())
a = list(map(int, input().split()))
a.sort()
ma = 0
if(n%2==0):
    for i in range(n//2):
        w = (a[i]+a[n-i-1])
        ma = max(w, ma)
else:
    ma = max(a)
    a.remove(ma)
    for i in range(len(a)//2):
        w = (a[i]+a[len(a)-i-1])
        ma = max(w, ma)
print(ma)  