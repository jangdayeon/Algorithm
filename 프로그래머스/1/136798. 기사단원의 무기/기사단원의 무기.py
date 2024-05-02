def solution(number, limit, power):
    yacksu = [0] * (number+1)
    for i in range(1,number+1): #약수 몇 개인지 하나하나 확인
        yacksu[i]=yacksuCheck(i)
    for i,y in enumerate(yacksu): #limit가 넘는 값 확인해서 power값으로 변경하기
        if y >limit:
            yacksu[i] = power
    return sum(yacksu)

def yacksuCheck(num):
    cnt = 0
    for n in range(1,int(num**(1/2))+1):
        if num%n==0:
            cnt +=1
            if n != num//n:
                cnt +=1
    return cnt
    