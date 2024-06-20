def solution(s):
    result = [0,0] 
    while s != '1':
        result[1] += s.count('0')
        result[0] += 1
        s = "".join(s.split('0'))
        s = format(int(len(s)),'b')
    return result