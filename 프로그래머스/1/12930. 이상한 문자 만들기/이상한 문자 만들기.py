def solution(s):
    s = s.lower()
    checking = True
    answer = ''
    for i in range(len(s)):
        if s[i]==' ':
            checking = True
            answer +=(' ')
        elif checking == True:
            answer+=(s[i].upper())
            checking = False
        else:
            answer+=(s[i])
            checking = True
    return answer