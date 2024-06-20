def solution(s):
    answer = ""
    for ss in s.split(" "):
        if ss == "" :
            answer += " "
        else :
            tmp = ss.lower()
            tmp = tmp[0].upper() + tmp[1:]
            answer += tmp + " "
    return answer[:-1]