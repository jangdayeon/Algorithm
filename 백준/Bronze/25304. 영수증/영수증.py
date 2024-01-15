have = int(input())
n = int(input())
total = 0
for i in range(n):
    sub, cnt = map(int, input().split())
    total+=sub*cnt
if(have==total):
    print("Yes")
else:
    print("No")