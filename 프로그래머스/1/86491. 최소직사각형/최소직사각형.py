def solution(sizes):
    big = []
    small= []
    for i,j in sizes:
        if(i>j):
            big.append(i)
            small.append(j)
        else:
            big.append(j)
            small.append(i)
    return max(big)*max(small)