#모음사전 문제랑 비슷함
#등비수열의 합 공식 사용 가능
def solution(n):
    ###자릿수 확인
    tmp = 0
    digit = 1 #n-1자리수 저장
    while tmp < n :
        tmp = (3*(3**digit-1))/(3-1)
        digit += 1
    
    digit -= 2
    tmp = (3*(3**digit-1))/(3-1)
    
    where = int(n - tmp) #124나라 숫자의 같은 자릿수 중 몇 번째 수인지
    ###앞자리부터 하나씩 확인
    geomatric = where
    answer = ""
    nara = {1:1,2:2,3:4}
    
    chchch = 0
    while digit > 0:
        for i in range(1,4):
            if 3**digit * i >= geomatric: #여길 수정 등비수열에서 개수로, =연산자 추가
                answer += str(nara[i])
                geomatric -=  3**digit * (i-1)
                break
        digit -=1
    return answer+str(nara[geomatric])
        
        