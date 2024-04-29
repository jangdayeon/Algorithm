def solution(a, b, n):
    answer = 0
    tmp = n
    while True:
        bottleSet = tmp//a # 20//3 == 6
        if bottleSet <= 0:
            break
        give = bottleSet*a # 6*3
        get = bottleSet*b #6*1
        tmp =  tmp-give+get
        answer+= get
    return answer