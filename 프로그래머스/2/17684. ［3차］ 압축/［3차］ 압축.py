def solution(msg):
    dic = {}
    for d in range(1,27):
        dic[chr(64+d)] = d
    d = 26
    pnt = 0
    now = ""
    result = []
    while pnt<len(msg):
        now += msg[pnt]
        pnt +=1
        if now not in dic:
            d+=1
            dic[now] = d
            result.append(dic[now[:-1]])
            now = ""
            pnt-=1
        if pnt == len(msg) :
            result.append(dic[now])
            return result