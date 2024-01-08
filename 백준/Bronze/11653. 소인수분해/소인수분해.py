import sys
input = sys.stdin.readline

n = int(input())

div = 2
if(n==0):
    print('')
else:
    while(n!=0):
        if(div > n):
            break
        elif(n%div==0):
            print(div)
            n = n /div
        else:
            div+=1
        