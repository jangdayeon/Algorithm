n = int(input())

x = [0] * 1000001
x[1] = 1
x[2] = 2
for i in range(3, len(x)):
    x[i] = (x[i-2]+x[i-1])%15746
print(x[n])