n = int(input())
x = [0] * 1001
x[1] = 1
x[2] = 3
for i in range(3, n+1):
    x[i] = ((x[i-2]*2)+x[i-1])%10007
print(x[n])