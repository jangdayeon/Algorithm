def solution(n):
    ret = list(map(int,list(str(n))))
    return ret[len(ret)::-1]