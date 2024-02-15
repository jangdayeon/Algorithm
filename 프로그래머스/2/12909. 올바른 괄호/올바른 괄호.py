#스택 이용
#( 이면 스택에 넣고, )이면 스택에서 팝하기, 만약에 팝하려고 하는데 스택 길이가 0이면 false 리턴하기
#전체 순회를 하면 true 리턴하기

def solution(s):
    stack = []
    for i in s:
        if(i == '('):
            stack.append('(')
        else:
            if(len(stack)>0):
                stack.pop()
            else:
                return False
    if(len(stack)==0):
        return True
    else :
        return False