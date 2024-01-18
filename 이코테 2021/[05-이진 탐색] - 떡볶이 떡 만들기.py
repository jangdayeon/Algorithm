import sys
input = sys.stdin.readline
import copy
n,m = map(int, input().split()) #떡의 수, 원하는 길이
dduck = list(map(int, input().split()))

rst = []
def binary_search(array, start, end):
    while(start <= end):
        mid = (start + end) //2
        dduckChk = list(map(lambda x:x-mid, dduck))
        dduckChkSum = 0
        for i in dduckChk:
            if(i>0):
                dduckChkSum+=i
        if (dduckChkSum>=m): #손님의 원하는 길이보다 길 때 rst에 추가
            rst.append(mid)
            start = mid + 1 #손님 덜 줘도 되니깐 칼이 오른쪽으로 이동
        else:
            end = mid -1 # 손님 더 줘야 하니깐 칼이 왼쪽으로 이동

binary_search(dduck, 1, max(dduck))
print(max(rst))
