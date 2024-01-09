import sys
input = sys.stdin.readline

x = []
y = []
for i in range(3):
    a, b = map(int, input().split())
    if(x.count(a)==1):
        x.remove(a)
    else:
        x.append(a)
    if(y.count(b)==1):
        y.remove(b)
    else:
        y.append(b)
        
print(x[0], y[0])