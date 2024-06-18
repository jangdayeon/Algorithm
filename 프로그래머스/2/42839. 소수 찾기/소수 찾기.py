from itertools import permutations

def solution(numbers):
    nums = set()
    for i in range(1,len(numbers)+1):
        a = map(lambda x:int("".join(x)), permutations(numbers,i))
        for aa in a:
            nums.add(aa)
    result = len(nums)
    for n in nums:
        if n < 2:
            result -=1
            continue
        for i in range(2,int(n**(1/2))+1):
            if n % i == 0:
                result -=1
                break
    return result
    
    