def solution(s):
    s = s[1:-1].split('},{')
    s[0] = s[0][1:]
    s[-1] = s[-1][:-1]
    s.sort(key = lambda x:len(x)) #튜플 차례대로 정렬
    
    result = []
    for ss in s : #1000000 최악
        temp = map(int, ss.split(',')) 
        a = set(result) ^ set(temp) 
        result.append(list(a)[0]) 
    return result