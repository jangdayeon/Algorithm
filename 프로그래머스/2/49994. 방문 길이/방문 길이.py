def solution(dirs):
    dirt = {'U':(1,0),'D':(-1,0),'L':(0,-1),'R':(0,1)}
    dirs = list(dirs)
    now = (0,0)
    answer = []
    for d in dirs:
        (dx,dy) = dirt[d]
        check = (now[0]+dx,now[1]+dy)
        if -5<=check[0]<=5 and -5<=check[1]<=5 :
            tmp = (now, check)
            tmp = sorted(tmp)
            if tmp not in answer:
                answer.append(tmp)
            now = check
    return len(answer)