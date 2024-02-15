#포켓몬 수의 반보다 경우의 수가 적을 경우 -> 다른 포켓몬 잡을 수 있는 최대의 수
#포켓몬 수의 반보다 경우의 수가 클 경우 -> 포켓몬 수의 반 리턴

def solution(nums):
    n = list(set(nums))
    if (len(n)>len(nums)//2):
        return len(nums)//2
    else:
        return len(n)