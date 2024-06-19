#모르겠어서 답을 찾아봤는데 sum이 큰 쪽이 작은 쪽으로 추가하는 방식으로 동작하면 된다는 것을 알게 됨
#총 경우의 수를 구하기 어려웠다.
#https://tae-hui.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%91%90-%ED%81%90-%ED%95%A9-%EA%B0%99%EA%B2%8C-%EB%A7%8C%EB%93%A4%EA%B8%B0-Level2-2022-KAKAO-TECH-INTERNSHIP
#위 블로그를 통해 3n-3이 최대 이동 수인 것을 알게되었다.
from collections import deque
def solution(queue1, queue2):
    q1, s1 = deque(queue1), sum(queue1)
    q2, s2 = deque(queue2), sum(queue2)
    for i in range(3*len(queue1)-3+1): 
        if s1 > s2 :
            tmp = q1.popleft()
            s1 -= tmp
            q2.append(tmp)
            s2 += tmp
        elif s1 < s2 :
            tmp = q2.popleft()
            s2 -= tmp
            q1.append(tmp)
            s1 += tmp
        else :
            return i
    return -1