#자료구조 - 원형 연결 리스트

#길이가 1~ len(elements)인 수열을 각각 구해 합의 종류를 구하기
#나는 노드로 원형 연결 리스트를 구현하지 않고, 나누기 연산을 통해 합을 계산할 것이다.
def solution(elements):
    result = set(elements) #길이가 1인 합 넣어둠
    temp = 0
    for i in range(2,len(elements)+1): #길이가 2이상인 것은 계산
        for j in range(len(elements)): #idx
            back = (len(elements)) - (j+i) #인덱스 범위 넘어가지 않는 선에서 숫자 몇 개?
            # 만약 back이 음수라면 리스트 범위를 벗어난 것이므로 그만큼 리스트 앞의 합도 계산
            if back >= 0 :
                result.add(sum(elements[j:j+i]))
            else :
                result.add(sum(elements[j:]+elements[:-back]))
    return len(result)
            
            