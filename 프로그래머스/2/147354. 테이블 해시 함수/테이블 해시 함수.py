def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x : (x[col-1],-x[0]))
    result = []
    for row in range(row_begin-1, row_end):
        result.append(sum(map(lambda x:x%(row+1), data[row])))
    rtn = 0 
    for r in result:
        rtn = rtn ^ r
    return rtn
        