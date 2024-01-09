import sys
input = sys.stdin.readline

while 1:
    i = input().strip()
    if(i == "0 0 0"):
        break
    a = list(map(int,i.split()))
    lo = max(a)
    if(a[0]+a[1]+a[2]<= 2*lo):
        print("Invalid")
    else:
        if(a[0]==a[1] and a[1]==a[2] and a[2]==a[0]):
            print("Equilateral")
        elif(a[0]==a[1] or a[1]==a[2] or a[2]==a[0]):
            print("Isosceles")
        else:
            print("Scalene")