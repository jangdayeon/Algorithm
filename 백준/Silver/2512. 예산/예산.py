import sys
input = sys.stdin.readline

n = int(input()) #지방 수
jibang = list(map(int, input().split())) #지방 별 예상요청
chong = int(input()) #총 예산
rst = []

def binary_search(start, end):
    while(start<=end):
        mid = (start+end)//2
        chk = list(map(lambda x:(mid if x>mid else x), jibang))
        if(sum(chk)<=chong):
            rst.append(mid)
            start = mid+1
        else:
            end = mid-1

if(sum(jibang)<=chong):
    print(max(jibang))
else:
    binary_search(1, max(jibang))
    print(max(rst))