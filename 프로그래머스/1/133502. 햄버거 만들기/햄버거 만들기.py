#replace로 풀다가 안됨
#테스트 케이스
#입력: [1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
#출력: 3
#위의 반례를 통해 replace로 이 문제를 해결할 수 없음을 알았고, stack을 이용해서 해결하고자 함
#세번째 틀림. 테케 5,12번에서 시간초과되는 문제 발생
def solution(ingredient):
    stack = []
    result = 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1,2,3,1]:
            # stack = stack[:-4] #이것의 시간 복잡도는 stack[a:b]일 경우 O(b-a)임
            # 그에 반해 pop()은 O(1)의 시간복잡도를 가짐
            # 참고로 del이나 remove의 경우 O(N)의 시간복잡도
            # for _ in range(4):
            #     stack.pop()
            del stack[-4:]
            result += 1
    return result