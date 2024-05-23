#stack 이용하여 올바른 괄호 문자열인지 확인

def solution(s):
    stack = [] #짝을 넣고 순회를 끝냈는데 stack에 원소가 남아있으면 false 아니면 true
    result = 0
    check_stack = True
    for i in range(len(s)):
        s = s[1:]+s[0]
        for ss in s[::-1]:
            if stack and ss =='{' and stack[-1]=='}':
                stack.pop()
            elif stack and ss =='[' and stack[-1]==']':
                stack.pop()
            elif stack and ss =='(' and stack[-1]==')':
                stack.pop()
            elif ss in ['}',']',')']:
                stack.append(ss)
            else :
                check_stack = False
                break
        if check_stack and len(stack) == 0 :
            result += 1  
        else:
            stack = []
        check_stack = True
    return result
        