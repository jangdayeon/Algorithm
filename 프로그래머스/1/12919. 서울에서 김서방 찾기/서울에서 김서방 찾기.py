def solution(seoul):
    for i in range(len(seoul)):
        if( seoul[i]=="Kim" ):
            return ''.join("김서방은 "+str(i)+"에 있다")
    return None