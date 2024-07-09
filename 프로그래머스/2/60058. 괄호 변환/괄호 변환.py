def is_balanced(s):
    stack = 0
    for char in s:
        if char == '(':
            stack += 1
        else:
            stack -= 1
    return stack == 0

def is_correct(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0

def reverse_parentheses(s):
    return ''.join(')' if char == '(' else '(' for char in s)

def solution(p):
    return do(p)

def do(p):
    if not p:
        return ''
    
    u, v = '', ''
    for i in range(2, len(p) + 1, 2):
        if is_balanced(p[:i]):
            u, v = p[:i], p[i:]
            break

    if is_correct(u):
        return u + do(v)
    else:
        return '(' + do(v) + ')' + reverse_parentheses(u[1:-1])
