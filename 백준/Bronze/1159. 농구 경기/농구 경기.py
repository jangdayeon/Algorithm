import sys
input = sys.stdin.readline

n = int(input())
li = [0] * 26
for i in range(n):
    a = list(input().strip())
    li[ord(a[0])-ord('a')] += 1
b= []
for i in range(len(li)):
    if(li[i]>=5):
        b.append(i)
if(len(b)>0):
    for i in b:
        print(chr(i+ord('a')), end='')
else:
    print("PREDAJA")