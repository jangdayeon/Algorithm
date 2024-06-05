#주식가격 문제와 같이 디폴트로 -1을 다 넣은다음에 만약에 stack에서 pop한 값보다 현재값이 더 크면 값을 갱신하도록 코드를 짜려고 한다. 
def solution(numbers):
    result = [-1] * len(numbers)
    stack = [0]
    for i in range(1,len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            j = stack.pop()
            result[j] = numbers[i]
        stack.append(i)
    return result