def solution(s): #스택 기억해
    stack = []
    for ss in s:
        if stack and stack[-1] == ss:
            stack.pop()
        else :
            stack.append(ss)
    return 0 if stack else 1