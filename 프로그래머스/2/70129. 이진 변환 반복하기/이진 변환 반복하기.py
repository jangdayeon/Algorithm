def solution(s):
    answer = [0,0] #변환 횟수, 제거된 0의 개수
    while True:
        answer[0] += 1 #횟수 +1
        answer[1] += s.count('0') # 0의 개수 구해서 더하기
        x = len(s.replace('0','')) #0들 제거
        if x == 1: #0 다 제거하고 길이를 쟀을 때 1이면 while문 종료
            break
        x = format(x,'b') #2진수로 변경
        s = x #2진수로 변경된 값을 s로 저장해 또 위 연산 시작
    return answer