import math
def solution(arr):
    if len(arr) == 1 :
        return arr[0]
    else:
        result = arr[0] * arr[1] // math.gcd(arr[0],arr[1])
        for i in range(2,len(arr)):
            result = result * arr[i] // math.gcd(result, arr[i])
        return result
