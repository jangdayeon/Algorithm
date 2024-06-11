def solution(x, y, n):
    list = [-1] * (y+1)
    list[x] = 0
    for i in range(x, y+1):
        if list[i] == -1:
            continue
        if i+n < y+1 and (list[i+n] == -1 or list[i+n] > list[i]+1): 
            list[i+n] = list[i]+1
        if i*2 < y+1 and (list[i*2] == -1 or list[i*2] > list[i]+1):
            list[i*2] = list[i]+1
        if i*3 < y+1 and (list[i*3] == -1 or list[i*3] > list[i]+1):
            list[i*3] = list[i]+1
    return list[y]