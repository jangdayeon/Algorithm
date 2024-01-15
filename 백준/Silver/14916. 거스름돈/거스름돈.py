import sys
input = sys.stdin.readline

a = int(input())
rest = a
rst = 0
while(rest>0):
    if(rest %5 ==0):
        rst+=rest//5
        rest%=5
    else:
        rst+=1
        rest-=2
print(rst if rest==0 else -1)