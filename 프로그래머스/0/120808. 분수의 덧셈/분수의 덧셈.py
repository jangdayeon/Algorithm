import math
def solution(numer1, denom1, numer2, denom2):
    result = [0,0]
    result[1] = (denom1*denom2)//math.gcd(denom1,denom2)
    result[0] = numer1*(result[1]//denom1) + numer2*(result[1]//denom2)
    while(math.gcd(result[0],result[1]) !=1):
        gcd = math.gcd(result[0],result[1])
        result[0] = result[0]//gcd
        result[1] = result[1]//gcd
    return result