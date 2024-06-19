def solution(s):
    stack = []
    for ss in s:
        if ss == "(":
            stack.append(0)
        elif stack:
            stack.pop()
        else :
            return False
    return False if stack else True