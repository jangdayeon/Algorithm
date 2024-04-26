def solution(food):
    answer = '0' #기본으로 물병두고
    for i in range(len(food)-1,0,-1): #0이후의 숫자 만들고
        if food[i]//2 > 0:
            print(i)
            answer+= food[i]//2*str(i)
    answer = answer[:0:-1]+answer #0과 좌우대칭이므로 0 이전의 숫자들도 합해주기
    return answer