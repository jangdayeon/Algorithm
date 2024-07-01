#시간복잡도 문제
#arrayA와 arrayB의 공약수 리스트를 제작
#차집합을 구해 가장 큰 수 리턴

import math
def solution(arrayA, arrayB):
    if (set(arrayA) & set(arrayB)): # arrayA와 arrayB에는 중복된 원소가 있을 수 있습니다.
        return 0
    
    aList = [arrayA[0]]
    bList = [arrayB[0]]
    for a in arrayA:
        aList[0] = math.gcd(a,aList[0])
    for b in arrayB:
        bList[0] = math.gcd(b,bList[0])
    
    for a in range(2,aList[0]//2):
        if aList[0] % a == 0:
            aList.append(a)
            aList.append(aList[0]//a)
            
    for b in range(2,bList[0]//2):
        if bList[0] % b == 0:
            bList.append(b)
            bList.append(bList[0]//b)
            
    if aList == [1]:
        aList.pop()
    else:
        aList.sort(reverse=True)
        
    if bList == [1]:
        bList.pop()
    else :
        bList.sort(reverse=True)
        
    result = 0
    for a in aList:
        for bb in arrayB:
            if bb % a == 0:
                break
        else:
            result = a if result<a else result
    for b in bList:
        for aa in arrayA:
            if aa % b == 0:
                break
        else:
            result = b if result<b else result

    return result