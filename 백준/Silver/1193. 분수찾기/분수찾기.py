import sys
input = sys.stdin.readline

n=int(input())

# 1 / 2,3 / 4,5,6 / 7,8,9,10

# [1,1] / [1,2][2,1] / [1,3][2,2][3,1] / [1,4][2,3][3,2][4,1]
# 0의 경우의 수 / 1
if(n==1):
    print("1/1")
else:
    fac = 1
    tmp = 1
    while (fac<n) :
        tmp+=1
        fac +=tmp # 1,3,6,10
    how = fac-n
    if(tmp%2!=0):
        print((1+how),'/',(tmp-how), sep='')
    else:    
        print((tmp-how),'/',(1+how), sep='')