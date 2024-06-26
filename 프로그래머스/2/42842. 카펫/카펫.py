def solution(brown, yellow):
    for i in range(3,(brown+yellow)//2+1):
        if (brown+yellow) % i == 0 and (i*2)+(((brown+yellow)//i)-2)*2 == brown:
            return [((brown+yellow)//i), i];
    return -1