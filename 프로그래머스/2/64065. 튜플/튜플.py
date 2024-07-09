def solution(s):
    result = []
    s = s.rstrip('}').lstrip('{').split("},{")
    for i in range(len(s)):
        s[i] = set(map(int, s[i].split(',')))
    s.sort(key = lambda x:len(x))
    se = set()
    for ss in s:
        a = ss-se
        aa = a.pop()
        result.append(aa)
        se.add(aa)
    return result