# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 기숙사 생활을 하는 학교에서 어떤 금요일(전원 귀가일)에는 모두 집으로 귀가를 한다.

# 오랜만에 집에 간 영일이는 아버지와 함께 두던 매우 큰 오목에 대해서 생각해 보다가
# "바둑판에 돌을 올린 것을 프로그래밍 할 수 있을까?"하고 생각하였다.

# 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
# n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.

# 예시
# d=[]                        #대괄호 [ ] 를 이용해 아무것도 없는 빈 리스트 만들기
# for i in range(20) :
#   d.append([])         #리스트 안에 다른 리스트 추가해 넣기
#   for j in range(20) : 
#     d[i].append(0)    #리스트 안에 들어있는 리스트 안에 0 추가해 넣기

# n = int(input())
# for i in range(n) :
#   x, y = input().split()
#   d[int(x)][int(y)] = 1

# for i in range(1, 20) :
#   for j in range(1, 20) : 
#     print(d[i][j], end=' ')    #공백을 두고 한 줄로 출력
#   print()                          #줄 바꿈

# 참고
# 리스트가 들어있는 리스트를 만들면?
# 가로번호, 세로번호를 사용해 2차원 형태의 데이터처럼 쉽게 기록하고 사용할 수 있다.
# 리스트이름[번호][번호] 형식으로 저장되어있는 값을 읽고 쓸 수 있고, 더 확장한 n차원의 리스트도 만들 수 있다.

# ...
# d=[]
# for i in range(20) : 
#   d.append([])
#   for j in range(20) :  
#     d[i].append(0)
# ... 

# 위와 같이, 모두 0이 채워진 2차원 리스트를 만드는 코드를 아래와 같은 방법으로 짧게 만들 수도 있다.
# ... [0 for j in range(20)]  #20개의 0이 들어간 [0, 0, 0, ... , 0, 0, 0] 리스트 
# 아래처럼 작성하면 위와 같은 리스트가 20개가 들어간 리스트를 한 번에 만들어 준다.

# d = [[0 for j in range(20)] for i in range(20)]

# 이러한 리스트 생성 방식을 List Comprehensions 라고 한다.

pan = [[0 for i in range(1,20)] for i in range(1,20)]

n = int(input())
for i in range(0,n):
    x,y = map(int, input().split())
    if(pan[x-1][y-1]!=1):
        pan[x-1][y-1]+=1    

for i in range(0, len(pan)):
    for j in range(0, len(pan[0])):
        print(pan[i][j], end=' ')
    print()