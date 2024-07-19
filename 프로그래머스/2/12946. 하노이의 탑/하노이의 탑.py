rtn = []

def solution(n):
    global rtn
    hanoi(n, 1, 3, 2)
    return rtn

def hanoi(n, fromP, toP, auxP):
    #hanoi(원반개수,시작,도착,보조)
    if n == 1: #1이면 시작에서 도착으로만 이동하면 됨
        rtn.append([fromP, toP])
        return
    hanoi(n-1, fromP, auxP, toP) #덩어리 원반들은 보조에 임시로 저장
    rtn.append([fromP, toP]) #가장 큰 원반은 도착지로 이동
    hanoi(n-1, auxP, toP, fromP) #덩어리 원반들을 다시 위와 같은 방식으로 해결