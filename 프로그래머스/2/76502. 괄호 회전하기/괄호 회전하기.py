from collections import deque

def solution(s):
    s = deque(s)
    result = 0
    for i in range(len(s)):
        stack = []
        t = s.popleft()
        s.append(t)
        allVisit = True
        for ss in list(s):
            if ss in ['[','(','{']:
                stack.append(ss)
            else:
                if ss == ']' and stack and stack[-1] == '[':
                    stack.pop()
                elif ss == ')' and stack and stack[-1] == '(':
                    stack.pop()
                elif ss == '}' and stack and stack[-1] == '{':
                    stack.pop()
                else:
                    allVisit = False
                    break
        if not stack and allVisit:
            result += 1
    return result
            