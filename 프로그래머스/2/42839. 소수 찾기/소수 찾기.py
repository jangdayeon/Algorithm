#첫 번째 아이디어
#일단 numbers 하나하나 나눠 list에 담고
#1개 선택하는 경우는 그냥 set에 경우의 수 모두 int로 넣고,
# permutations 함수를 이용하여 2부터 위 list의 길이까지 구한 다음
#set에 int로 바꾼 후 집어 넣어서 중복 방지하기
#소수 판별하고 len 리턴하기

from itertools import permutations
import copy
import math
def solution(numbers):
    nums = list(numbers)
    beforeSet = copy.deepcopy(nums)
    
    for i in range(2, len(nums)+1):
        a = permutations(nums, i)
        for j in a:
            b = int("".join(j))
            beforeSet.append(b)
    answer0 = list(map(int, beforeSet))
    print(*answer0)
    #여기부터 소수 판별
    if(len(answer0)==0 or sum(answer0)==0):
        return 0
    forNum = [True for _ in range(max(answer0)+1)]
    forNum[0],forNum[1] = False,False
    for i in range(2, int(math.sqrt(len(forNum)))+1):
        if forNum[i] == True: #소수일 경우, 이 소수의 배수들 싹 다 지우기
            j = 2
            while i*j < len(forNum):
                forNum[i*j] = False
                j+=1
    answer = []
    for i in answer0:
        if(forNum[i]==True):
            answer.append(i)
    # print(*answer)
    return len(set(answer))