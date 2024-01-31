import sys
input = sys.stdin.readline

n = int(input())
t = list(input().strip())

now = t[0]
li = [now]
change = 0
for i in t:
    if(i != now):
        now = i
        li.append(now)

mini = li.count('B') if li.count('B')<li.count('R') else li.count('R')
print(mini+1)