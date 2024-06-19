#작은 수 부터 삭제하려고 했는데 '앞에서'부터 작은 수를 삭제해야 하는데 아이디어가 안떠올라 답 확인했다.

#number을 다 돌아도 k만큼 삭제 안되는 경우가 있어서 그걸 return할 때 고려해서 코드를 짜야 함

from collections import deque
def solution(number, k):
    result = [] #stack
    for n in number:
        while result and k > 0 and result[-1] < n :
            k -= 1
            result.pop()
        result.append(n)
    return "".join(result[:-k] if k>0 else result)