def solution(lottos, win_nums):
    result = [0,0]
    lottos.sort()
    win_nums.sort()
    for l in lottos:
        if l == 0 :
            result[1]+=1
        else:
            for w in win_nums:
                if w == l:
                    result[0]+=1
                    result[1]+=1
                    break
    rtn = {0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    return rtn[result[1]],rtn[result[0]]