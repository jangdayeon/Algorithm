#괄호 맞추기랑 같은데 어렵게 생각해서 못풀고 정답지 확인함,,
def solution(s):
    stack = []
    for i in range(len(s)):
        if len(stack) == 0: #스택이 비었을 경우
            stack.append(s[i])
        elif stack[-1] == s[i] : #짝인 숫자일 경우
            stack.pop()
        else: #짝이 아닐 경우
            stack.append(s[i])
    if len(stack)==0:
        return 1
    else :
        return 0
            