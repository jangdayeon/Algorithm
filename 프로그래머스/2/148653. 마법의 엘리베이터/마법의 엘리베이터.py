#맨 끝자리수부터 확인해서 구하기 
# 답 확인함
#나는 나보다 앞자리수한테 1만큼 빌려서 사용할 생각을 했는데, 앞자리수까지 이동한다고 생각해야 문제 풀기 편함
#나누기 연산을 통해 맨 끝자리 구하는 거 기억하기
def solution(storey):
    result = 0
    while storey:
        chk = storey % 10 #나누기 연산을 통해 맨 끝자리 구하기
        if chk < 5:
            result += chk
            storey -= chk
        elif chk > 5:
            result += 10-chk
            storey += (10-chk)
        else :
            if storey >= 10 and storey % 100 - chk > 40:
                result += 10-chk
                storey += (10-chk)
            else :
                result += chk
                storey -= chk
        storey //= 10
    return result