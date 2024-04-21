def solution(n):
    n_3 = int(tenToThree(n))
    n_reversed3 = str(n_3)[::-1]
    return int(n_reversed3,3)
    
def tenToThree(n):
    remainder = "" #3으로 나눈 나머지값들을 저장할 변수
    quotient = n #3으로 나눈 몫 저장할 변수
    while True:
        remainder+=str(quotient%3)
        quotient = quotient//3
        if(quotient//3==0):
            remainder+=str(quotient)
            return remainder[::-1]
    