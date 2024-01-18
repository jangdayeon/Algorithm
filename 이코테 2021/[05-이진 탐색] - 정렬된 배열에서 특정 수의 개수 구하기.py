import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

n,x = map(int, input().split())
nums = list(map(int, input().split()))

def count_by_range():
    right_index = bisect_right(nums, x)
    left_index = bisect_left(nums, x)
    return right_index-left_index

print(count_by_range())