rtn = 0
def solution(numbers, target):
    recursion(numbers,target, 0, 0)
    return rtn

def recursion(numbers, target, n_idx, cal): #리스트, 타겟, 현재 인덱스, 지금까지 계산한 값
    global rtn
    if n_idx == len(numbers) :
        if target == cal :
            rtn += 1
        return
    recursion(numbers, target, n_idx + 1, cal + numbers[n_idx])
    recursion(numbers, target, n_idx + 1, cal - numbers[n_idx])   