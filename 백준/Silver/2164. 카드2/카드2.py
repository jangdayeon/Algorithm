import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
queue = deque( [i for i in range(1,n+1)] )
if(len(queue)!=1):   
    while True:
        queue.popleft()
        if(len(queue)<=1):
            break
        queue.append(queue.popleft())
print(queue.popleft())