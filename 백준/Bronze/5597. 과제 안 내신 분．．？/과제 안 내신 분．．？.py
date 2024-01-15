import sys
input = sys.stdin.readline

cl = [i for i in range(1,31)]

for i in range(28):
    a = int(input())
    cl.remove(a)
  
for i in range(len(cl)):
    print(cl[i])