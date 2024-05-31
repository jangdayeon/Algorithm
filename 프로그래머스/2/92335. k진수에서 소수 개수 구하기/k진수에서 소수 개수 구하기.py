#많이 틀림. 소수 판별에서 아리토스테네스의 체를 이용했는데, k 이하의 모든 소수를 구하는 방식이었어서 적절치 않았음
# 제곱근을 이용한 소수 판별로 문제를 해결하면 된다는 것을 알게됐다.
# 추가로 continue랑 break,, 이중 반복문 기준으로 생각하지 말고 1중으로만 생각해라
def solution(n, k):
    muck = 0 #몫
    rest = "" #나머지
    if k == 10:
        rest = str(int(n))
    else:
        while True: #진수 변환
            rest += str(n % k)
            n = n // k
            if n < 1 :
                break
        rest = rest[::-1]
    #여기부터는 0을 기준으로 문자열 나누기
    rest = rest.split('0')
    
    for r in range(rest.count('')):
        rest.remove('')
    print(rest)
    rest = list(map(int, rest))
    maxi = max(rest)
    
    # #소수 구하기(에라토스테네스의 체)
    # sosu = [True] * (maxi+1)
    # sosu[0], sosu[1] = True,False
    # for i in range(2, maxi+1):
    #     if sosu[i]:
    #         j = 2 
    #         while j*i < maxi+1:
    #             sosu[j*i] = False
    #             j += 1
    #소수인 값 몇 갠지 구하기
    # result = 0
    # for r in rest:
    #     if sosu[r] :
    #         result += 1
    # return result
    
    result = 0
    #소수 구하기(제곱근)
    for i in rest:
        sosu = True
        if i <= 1: 
            pass
        else:
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    sosu = False
                    break
            if sosu:
                result += 1
    return result
    