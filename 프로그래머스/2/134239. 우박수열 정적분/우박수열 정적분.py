def solution(k, ranges):
    # find x
    x = [k]
    idx, tmp =1,k
    while tmp > 1 :
        if tmp % 2 == 0:
            tmp /= 2
        else :
            tmp = tmp * 3 + 1
        x.append(tmp)

    # find area
    area = [0]
    for i in range(len(x)-1):
        area.append(area[i]+(x[i]+x[i+1])/2)
    
    #calculate
    result = []
    for (s,e) in ranges:
        if s <= len(area)-1+e :
            result.append(area[len(area)-1+e]- area[s])
        else :
            result.append(-1.0)
    
    return result
    