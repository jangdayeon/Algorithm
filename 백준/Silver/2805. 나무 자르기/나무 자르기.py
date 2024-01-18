import sys
input = sys.stdin.readline

n, m = map(int, input().split())
h = list(map(int, input().split()))

max_rst = 0

def binary_search(start, end):
    global max_rst
    while start <= end:
        mid = (start + end) // 2
        hh = [(0 if mid >= x else x - mid) for x in h]
        if sum(hh) >= m:
            max_rst = max(max_rst, mid)
            start = mid + 1
        else:
            end = mid - 1

binary_search(1, max(h))
print(max_rst)
