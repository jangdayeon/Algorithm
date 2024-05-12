#짝수이면 자기 앞 참가자와, 홀수이면 자기 뒤 참가자와 붙음
#한 번 틀림. if abs(a-b) == 1 이면 리턴하도록 했는데 그럼 3,4일 경우가 문제가 됨
#두 번 틀림. a와 b 중 작은 수는 홀수, 큰 수는 짝수여야 함
def solution(n,a,b):
    answer = 0
    while True:
        answer += 1
        if abs(a-b) == 1 and (min(a,b)%2==1 and max(a,b)%2==0):
            return answer
        if a % 2 == 0 :
            a = a/2
        else :
            a = (a+1)/2
        if b % 2 == 0 :
            b = b/2
        else :
            b = (b+1)/2
        print(a,b)
    return -1