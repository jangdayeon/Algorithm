def solution(rows, columns, queries):
    pan = [[0] * columns for _ in range(rows)]
    result = []
    
    tmp = 1
    for i in range(rows): #pan 초기화
        for j in range(columns):
            pan[i][j] = tmp
            tmp+=1
         
    for query in queries: #right,down,left,up 방향으로 이동해야하는 위치 각각 저장 후 숫자 이동
        [start_r, start_c, end_r, end_c] = map(lambda x:x-1, query)
        right = [(start_r,i) for i in range(start_c,end_c)]
        down = [(i,end_c) for i in range(start_r,end_r)]
        left = [(end_r,i) for i in range(end_c,start_c,-1)]
        up = [(i,start_c) for i in range(end_r,start_r,-1)]
        (start, mini0, pan) = lineChange(pan, right, pan[start_r][start_c], (0,1))
        (start, mini1, pan) = lineChange(pan, down, start, (1,0))
        (start, mini2, pan) = lineChange(pan, left, start, (0,-1))
        (start, mini3, pan) = lineChange(pan, up, start, (-1,0))
        result.append(min(mini0,mini1,mini2,mini3))
    return result
        
def lineChange(pan, line, start, direct): #숫자 이동 함수
    mini = 1e9
    for (i,j) in line:
        tmp = pan[i+direct[0]][j+direct[1]]
        pan[i+direct[0]][j+direct[1]] = start
        mini = min(mini, pan[i+direct[0]][j+direct[1]])
        start = tmp
    return (start,mini,pan)