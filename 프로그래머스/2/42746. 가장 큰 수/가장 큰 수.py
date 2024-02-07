def solution(numbers):
    numbers = map(str, numbers)
    a = list(map(lambda x:x*3, numbers))
    a.sort(reverse=True)
    a = list(map(lambda x:x[0:len(x)//3], a))
    
    answer = str((int(''.join(a))))
    return answer