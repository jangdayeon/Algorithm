def solution(numbers):
    answer = 45 #0~9까지 합
    for n in numbers:
        answer -=n
    return answer