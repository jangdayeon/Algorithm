import sys
input = sys.stdin.readline

a = list(input().strip().split('.'))
chk = True
for i in a:
    rest = len(i)
    rst = []
    if(len(i)%2==0):
        rst.append("AAAA"*(rest//4))
        rest -= rest//4*4
        rst.append("BB"*(rest//2))
        rest -= rest//2*2
        a[a.index(i)] = ''.join(rst)
    elif(len(i)==0):
        a[a.index(i)] ='.'
    else:
        chk=False

print('.'.join(a) if chk == True else -1)