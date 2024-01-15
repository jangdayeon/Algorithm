import sys
input = sys.stdin.readline

def cha(a):
    if(a=="A+"):
        return 4.5
    elif(a=="A0"):
        return 4.0
    elif(a=="B+"):
        return 3.5
    elif(a=="B0"):
        return 3.0
    elif(a=="C+"):
        return 2.5
    elif(a=="C0"):
        return 2.0
    elif(a=="D+"):
        return 1.5
    elif(a=="D0"):
        return 1.0
    elif(a=="F"):
        return 0.0
    else:
        return 0

rst = 0
totalSub = 0
for _ in range(20):
    a = input().split()
    if(a[2]=="P"):
        continue
    else:
        rst += float(a[1])*cha(a[2])
        totalSub += float(a[1])
rst = rst/totalSub

print('%0.6f'%rst)