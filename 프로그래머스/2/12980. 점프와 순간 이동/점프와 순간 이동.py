def solution(n):
    result = 0
    while n :
        if n % 2 != 0 :
            n -= 1
            result += 1
        n //= 2
    return result