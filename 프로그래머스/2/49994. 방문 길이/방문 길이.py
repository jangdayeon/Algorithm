#첫번째 틀림. 하나 빼고 다 틀림 하하.. 런타임 에러가 주를 이뤘는데,<=9까지 줬어야 함
#두번째 틀림. 잘못 풀고 있었음. 점->점으로 선분이 어디서 어디로 이어졌는지 저장해야 할 것 같다.
#세번째 틀림. 이젠 런타임 에러를 안 떴는데, 문제 많이 틀림
    # -> "ULDRRULDULDR" 일 때 7이 떠야하는데 8로 뜨는 문제 -> UDRL의 각 경우로 나눠 구하게 함
#네번째 틀림. UD와 LR의 범위가 다름을 다시 if문으로 나눠 걸러줬음
def solution(dirs):
    direction = {"U":(-1,0), "D":(1,0), "R":(0,1), "L":(0,-1)}
    garo = [ [False] * 10  for _ in range(11) ] # 가로 줄 #9,10
    saero = [ [False] * 11  for _ in range(10) ] # 세로 줄 #10,9
    start = (5,5) #점
    result = 0
    for i in range(len(dirs)):
        d = dirs[i]
        a,b = direction[d] 
        if 0<=start[0]+a<=10 and 0<=start[1]+b<=10:
            start = (start[0]+a, start[1]+b)
            if d == "U" and saero[start[0]][start[1]] == False:
                result += 1
                saero[start[0]][start[1]] = True
            elif d == "D" and saero[start[0]-1][start[1]] == False:
                result += 1
                saero[start[0]-1][start[1]] = True
            elif d == "L" and garo[start[0]][start[1]] == False:
                result += 1
                garo[start[0]][start[1]] = True
            elif d == "R" and garo[start[0]][start[1]-1] == False:
                result += 1
                garo[start[0]][start[1]-1] = True
    return result
    
    
    