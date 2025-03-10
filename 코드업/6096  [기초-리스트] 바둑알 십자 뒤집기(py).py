# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 부모님을 기다리던 영일이는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아 놓고 놀다가...

# "십(+)자 뒤집기를 해볼까?"하고 생각했다.

# 십자 뒤집기는
# 그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후, 
# 다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다.
# 어떤 위치를 골라 집자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다.

# 바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
# n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

# 예시
# ...
# for i in range(n) :
#   x,y=input().split()
#   for j in range(1, 20) :
#     if d[j][int(y)]==0 :
#       d[j][int(y)]=1
#     else :
#       d[j][int(y)]=0

#     if d[int(x)][j]==0 :
#       d[int(x)][j]=1
#     else :
#       d[int(x)][j]=0
# ...

# 참고
# 리스트가 들어있는 리스트를 만들면?
# 가로번호, 세로번호를 사용해 2차원 형태의 데이터처럼 쉽게 기록하고 사용할 수 있다.
# 리스트이름[번호][번호] 형식으로 저장되어있는 값을 읽고 쓸 수 있다.

pan = [0 for _ in range(0,19)]

for i in range(0,19):
    pan[i] = list(map(int, input().split()))
    
n = int(input())
for i in range(0,n):
    x,y = map(int, input().split())
    x -=1
    y -=1
    
    for j in range(0,19):
        pan[j][y] = (0 if pan[j][y]==1 else 1)
    for j in range(0,19):
        pan[x][j] = (0 if pan[x][j]==1 else 1)

for i in range(0,19):
    for j in range(0,19):
        print(pan[i][j], end=' ')
    print()

#tuple to list는 그냥 list(tuple) 넣으면 된다!!
#그리고 for문에 인덱스 안쓰면 _로 남겨놔도 된다.