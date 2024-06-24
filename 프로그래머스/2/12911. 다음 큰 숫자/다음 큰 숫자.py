def solution(n):
    result = n+1
    one_count = format(n,'b').count('1')
    while format(result,'b').count('1') != one_count :
        result +=1
    return result