import sys
input= sys.stdin.readline

n = int(input()) # 병사 몇 명
soldier = list(map(int, input().split())) # 병사들

#가장 긴 증가하는 부분 수열 (LIS) 알고리즘을 사용해야 한다.
# 이 알고리즘은 4, 2, 5, 8, 4, 11, 15 순(오름차순)으로 정렬하고 싶을 때

# D[i]= array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이일 경우
# 모든 0 <= j < i 에 대하여, D[i] = max(D[i], D[j]+1) if array[j]<array[i]

soldier = soldier[::-1]
print(*soldier)
cnt = [1] * len(soldier)
for i in range(1,len(soldier)):
    where = [0]
    for j in range(0,i):
        if(soldier[i]>soldier[j]):
            where.append(cnt[j])
    cnt[i] += max(where)

print(cnt[len(cnt)-1])