#한 번 틀림. 이중 for문을 사용해서.. n이 백만까지 가므로, O(N) 시간을 맞춰야 함
# 2중 for문 어떻게 안써야할지 모르겠어서,, 일단 1열의 리스트를 만든다음 인덱스 접근함
#두 번 틀림. 시간초과는 안나는데 컴파일 에러가 뜨는 문제 발생 -> 리스트 한 줄로 하면 memoryerror 발생..
#세 번 틀림. li = [[i+1 for i in range(n)] for _ in range(n)] 이렇게 2차원 배열 만드는 것 자체가 문제여서 리스트를 만들지 않고 계산식을 세워 문제를 풀어보려고 함.
#네 번 틀림. 테스트케이스 1번이 틀리는데,  n이 1일 경우는 예외로 빼줘야 함
def solution(n, left, right):
    result = []
    if n == 1:
        return [1]
    for i in range(left, right+1):
        a = i // n + 1#행
        b = i % n #열
        if a > b :
            result.append(a)
        else :
            result.append(b+1)
    return result