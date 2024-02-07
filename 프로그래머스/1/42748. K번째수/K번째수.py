def solution(array, commands):
    answer = []
    for c in commands:
        i,j,k = c
        a = array[i-1:j:]
        a.sort()
        answer.append(a[k-1])
    return answer