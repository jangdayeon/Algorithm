#조합 문제
#안 입는 경우도 조건에 두어 계산 후 아무것도 안 입는 경우를 빼주기

def solution(clothes):
    closet = dict()
    for c in clothes: #분류별로 옷 나누기
        if c[1] in closet:
            closet[c[1]] +=1
        else :
            closet[c[1]] = 1

    result = 1
    for c in closet: #조합 계산하기
        result *= closet[c]+1
    return result-1