def solution(n, m, section):
    answer = 0

    h = section[0] #처음 시작

    for v in section: #색을 칠해야 하는 곳
        if(v - h + 1 > m): #색을 칠해야 하는 곳 - 색 칠하기 완성한 곳+1>롤러의 길이
            answer += 1
            h = v

    return answer + 1