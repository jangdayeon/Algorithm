#멀리뛰기, 바닥공사 문제와 유사한데, dp로 어떻게 푸는지 까먹어서 답지를 확인했다.
#이 문제 풀이법은 반복해서 다양하게 나오는 것 같으니 잘 확인하기
#기억해야 할 점은 팩토리얼을 통해 조합을 구하는 문제를 s(n) = s(n-2)+s(n-1)으로 해결할 수 있다는 점이다.
def solution(n):
    list = [0] * (n+1)
    list[1] = 1
    list[2] = 2
    for i in range(3,len(list)):
        list[i] = (list[i-2]+list[i-1]) % 1000000007
    return list[n]