def solution(s):
    numbers = list(map(int, s.split()))
    maxi = max(numbers)
    mini = min(numbers)
    return f"{mini} {maxi}"
