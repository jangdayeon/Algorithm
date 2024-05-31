# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
def solution(n, t, m, p):
    #nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '0', '1', '1', '1', '2']
    num_str = ""
    for i in range(t*m):
        num_str += jinbup(n,i)
    nums = list(num_str)[p-1::m] #튜브의 첫 순서부터 +m 씩해서 튜브의 차례만 골라냄
    return "".join(nums[:t]) #구해야하는 숫자 개수만큼 리스트 슬라이싱하고 문자열로 리턴
    
def jinbup(n, num): #진법, 숫자
    rest = ''
    if n == 10 or num == 0: #10진법이거나 n == 0일 경운 그대로 리턴
        return str(num)
    while num > 0 :
        if num%n >= 10 : # 10~15는 각각 대문자 A~F로 출력
             rest += chr((num%n) - 10 + ord('A')) 
        else: 
            rest += str(num%n)
        num = num // n
    return rest[::-1]