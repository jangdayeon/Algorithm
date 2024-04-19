def solution(arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1,arr2):
        answer.append(list(map(lambda x,y:x+y, a1,a2)))
    return answer