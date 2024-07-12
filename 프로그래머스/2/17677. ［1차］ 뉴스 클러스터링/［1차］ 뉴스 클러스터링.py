def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    ms1, ms2 = multiset(str1), multiset(str2)
    s1, s2 = set(list(ms1)), set(list(ms2))
    if not s1 and not s2 : return 65536

    s12And = s1 & s2
    s12Or = s1 | s2
    
    up = len(s12And)
    for ss in s12And:
        mini = min(ms1[ss], ms2[ss])
        up += mini - 1
        
    down = len(s12Or)
    for ss in s12Or:
        if ss in ms1 and ss in ms2:
            maxi = max(ms1[ss],ms2[ss])
            down += maxi -1
        elif ss in ms1:
            down += ms1[ss] -1
        elif ss in ms2:
            down += ms2[ss] -1
            
    return int((up/down)*65536)
    
def multiset(s):
    result = {}
    for i in range(1,len(s)):
        if ord('a')<=ord(s[i-1])<=ord('z') and ord('a')<=ord(s[i])<=ord('z'):
            ss = s[i-1:i+1]
            if ss in result:
                result[ss] += 1
            else:
                result[ss] = 1
    return result