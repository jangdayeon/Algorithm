def solution(s):
    answer = 0
    x = s[0]
    divideStart = 0
    for i in range(1,len(s)):
        if s[divideStart:i].count(x) * 2 == i-divideStart:
            # print(i, s[divideStart:i])
            answer +=1
            x = s[i]
            divideStart = i
        
    return answer+1