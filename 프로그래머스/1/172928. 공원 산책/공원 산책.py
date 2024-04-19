def solution(park, routes):
    direction = {"N":[-1,0], "S":[1,0], "W":[0,-1], "E":[0,1]} # 1. direction을 dict으로 저장
    # 2. S 찾아 location에 저장
    location = [0,0] 
    for p in range(len(park)):
        if park[p].find("S")>-1:
            location = [p,park[p].find("S")]
            break
    # 3. routes에 적힌대로 이동하기 구현
    for r in routes:
        op, n = r.split(" ")
        nextLocation = list(map(lambda x,y:x*int(n)+y, direction[op],location)) #이동성공시 바뀔 위치
        if -1<nextLocation[0]<len(park) and -1<nextLocation[1]<len(park[0]):
            if XCheck(direction, op, int(n), park, location)==False: #가는 길에 X를 발견하면 True
                location = nextLocation
    return location

def XCheck(direction, op, n, park, location):
    for i in range(1,n+1):
        if park[direction[op][0]*i+location[0]][direction[op][1]*i+location[1]]=="X":
            return True
    return False