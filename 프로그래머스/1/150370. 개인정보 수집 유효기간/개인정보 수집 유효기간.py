#한 번 틀림. date함수를 썼는데 컴파일 에러 발생
#두 번 틀림. 오름차순 정렬X
#세 번 틀림. 12월일 경우를 고려X -> 수정
def solution(today, terms, privacies):
    terms_dic = {}
    result = []
    for t in terms:
        terms_dic[t[0]] = int(t[2:])
        
    for i,pri in enumerate(privacies):
        getDate, dateType = pri.split(" ")
        getDate = list(map(int,getDate.split(".")))
        getDate[1] += terms_dic[dateType]
        if getDate[1] % 12 == 0:
            getDate[0] += getDate[1] // 12 - 1
            getDate[1] = 12
        else:
            getDate[0] += getDate[1] // 12
            getDate[1] = getDate[1] % 12
            
        if getDate[0] <= int(today[:4]):
            if getDate[0] < int(today[:4]): #년 비교
                result.append(i+1)
            else : #년이 같으면
                if getDate[1] <= int(today[5:7]):
                    if getDate[1] < int(today[5:7]): #월 비교
                        result.append(i+1)
                    else : #월이 같으면
                        if getDate[2] <= int(today[8:]): #일 비교
                            result.append(i+1)       
    return sorted(result)
        