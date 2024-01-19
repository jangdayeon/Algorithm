import sys
input = sys.stdin.readline

# 이것도 점화식 못 구해서,, 답지 찾아봄
# 점화식 : a_n = min(a_n/5, a_n/3, a_n/2, a_n-1) +1 

# 상향식(보텀업)을 통해 구하겠다
a = int(input())

x = [-1] * (a+1)
x[1] = 0
x[2] = 1
x[3] = 1
x[4] = 2
x[5] = 1

for i in range(6,a+1):
    what = []
    for j in [2,3,5]:
        if(i%j==0):
            what.append(x[i//j])
    what.append(x[i-1])
    x[i] = min(what) +1
print(x[a])