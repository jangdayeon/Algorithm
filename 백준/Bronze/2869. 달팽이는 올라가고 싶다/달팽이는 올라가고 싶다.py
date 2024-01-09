import sys
input = sys.stdin.readline

import math
a,b,v= map(int, input().split())

올라간거리= (v-b)/(a-b)
print(math.ceil(올라간거리))