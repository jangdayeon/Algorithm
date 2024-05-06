#스택 이용
#스택 한 곳에 전책 저장, 다른 한 곳엔 )을 저장하는데, 만약 순회를 돌다가 (이 나왔을 때 )들의 len 이 0이면 false리턴 전체 순회를 했을 시 true리턴
def solution(s):
    stackB = [] #)
    for s in list(s)[::-1]:
        if s == ')':
            stackB.append(')')
        else:
            if len(stackB):
                stackB.pop()
            else:
                return False
    return True if len(stackB)==0 else False
                