#첫번째 아이디어
#brown+yellow 하고, 이 수가 어떤 수로 나눠지는지 (3이상에 brown과 yellow 수 미포함) 구하고
# brown = brown - (큰 수 *2) 하고, ( brown /2 ) + 2 == 작은 수이면 true로 리턴하기

def solution(brown, yellow):
    by = brown + yellow
    suu = []
    for i in range(3,by):
        #[작은 값, 큰 값]이 들어오기 시작하면 break
        if(by//i < i):
            break
        if(by % i ==0): #나머지가 0이면
            suu.append([by//i, i]) #값 추가하기([큰 값, 작은 값])
    # print(*suu) 
    
    for big, small in suu:
        a = brown - (big*2)
        if(a/2 +2 == small):
            return [big,small]
    return None