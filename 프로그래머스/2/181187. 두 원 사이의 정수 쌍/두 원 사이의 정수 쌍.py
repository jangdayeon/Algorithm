#원의 방정식(원점이 0일 경우) -> x^2 + y^2 = r^2
from math import sqrt,floor,ceil
def solution(r1, r2):
    if(r1 == r2) : return 4
    result = 4 #큰 원이 x절편과 y절편 지나는 곳의 개수
    tmp = 0
    for x in range(1, r2):
        r2_y = sqrt(r2**2 - x**2)
        r1_y = 0 if x>r1 else sqrt(r1**2 - x**2)
        tmp += floor(r2_y)-ceil(r1_y)+1
    return result + tmp*4