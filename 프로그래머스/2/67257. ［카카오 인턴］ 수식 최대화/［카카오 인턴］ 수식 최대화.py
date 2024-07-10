import re
from collections import deque

def solution(expression):
    nums = deque(re.split(r'[*+-]',expression))
    oprs = re.split(r'[0-9]+',expression)[1:-1]
    combi = [('*','+','-'),('*','-','+'),('+','*','-'),('+','-','*'),('-','+','*'),('-','*','+')]
    result = 0
    for com in combi:
        nums_t = []
        oprs_t = []
        for n in nums:
            nums_t.append(n)
        for o in oprs:
            oprs_t.append(o)
            
        result = max(result,calculator(com,nums_t,oprs_t))

    return result

def calculator(com, nums, oprs):
    for c in com: #('*', '+', '-')
        i = 0
        while oprs: #['-', '*', '-', '+']
            if i == len(oprs):
                break
            if oprs[i] == c:
                n = eval(str(nums[i])+oprs[i]+str(nums[i+1])) #연산
                nums.pop(i) #연산한 숫자 하나 빼고
                nums[i] = n #값 변경
                oprs.pop(i) #연산한 연산자 하나 빼기
            else: #해당 연산자가 찾아보고 있는 우선순위 연산자가 아닐 경우 인덱스 옮기기
                i+=1
    return abs(nums[0])
                