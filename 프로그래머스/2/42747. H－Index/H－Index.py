def solution(citations):
    for i in range(max(citations),-1,-1):
        up_down = [0,0]
        for c in citations:
            if c >= i :
                up_down[0] += 1
            else:
                up_down[1] += 1
        if up_down[0] >= i and up_down[1] <= i :
            return i