def solution(arr):
    if(len(arr)==1):
        return [-1]
    else:
        mini = min(arr)
        arr.remove(mini)
        return arr