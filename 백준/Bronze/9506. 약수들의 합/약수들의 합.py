import sys
input = sys.stdin.readline

while 1:
    a = int(input())
    if(a==-1):
        break
    yak = []
    for i in range(1,a):
        if(a%i==0):
            yak.append(i)
    if(sum(yak)==a):
        print(a, "=", " + ".join(str(i) for i in yak))
    else:
        print(a, "is NOT perfect.")