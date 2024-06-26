from math import gcd

def solution(arr):
    result = arr[0]
    for i in range(1,len(arr)):
        result = (result*arr[i]) // gcd(result,arr[i]) 
    return result