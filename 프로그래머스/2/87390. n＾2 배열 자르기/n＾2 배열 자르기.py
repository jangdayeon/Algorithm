def solution(n, left, right):
    result = []
    for i in range(left,right+1):
        a = i // n #행
        b = i % n #열
        if a <= b:
            result.append(b+1)
        else:
            result.append(a+1)
    return result