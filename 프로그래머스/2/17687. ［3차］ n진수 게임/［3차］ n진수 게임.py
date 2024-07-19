def solution(n, t, m, p):
    nums = []
    game = "0"
    for i in range(1, t*m+1): #1,2,3 .. 진법 변환한 수 game변수에 이어붙이기
        game += transJinsoo(n,i)
    rtn = ""
    for g in list(game)[p-1:t*m:m]: #튜브 차례만 빼서 rtn에 저장하기
        rtn += g
    return rtn 
    
def transJinsoo(n,i):
    trans = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    rtn = ""
    while i>0:
        div, mod = divmod(i,n)
        if mod < 10 :
            rtn += str(mod)
        else :
            rtn += trans[mod]
        i = div
    return rtn[::-1]