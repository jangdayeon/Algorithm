n = int(input())
    
x = [-1, -1] * (n+1) #맨 뒷글자가 0인 경우의 수, 1인 경우의 수
x[1] = [0,1]
x[2] = [1,0]
for i in range(2,n+1):
    x[i] = [x[i-1][0]+x[i-1][1],x[i-1][0]]
print(sum(x[n]))