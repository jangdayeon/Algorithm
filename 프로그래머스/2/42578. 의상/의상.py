def solution(clothes):
    dic = {}
    for c in clothes:
        if c[1] in dic:
            dic[c[1]]+=1
        else:
            dic[c[1]] =1           
    result = 1
    for d in dic.values():
        result *=(d+1)
    return result -1