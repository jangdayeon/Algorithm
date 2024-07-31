#답 확인함
#일단 stack의 맨 나중에 들어온 애가 현재값보다 크면 pop해줘서 중간에 엄청 큰 값이 있어도 상관이 없다.
def solution(prices):
    stack = []
    # answer을 max값으로 초기화  
    answer = [ i for i in range (len(prices) - 1, -1, -1)]
    for i,p in enumerate(prices):
        while stack and prices[stack[-1]] > p :
            j = stack.pop()
            answer[j] = i-j
        stack.append(i)
    return answer