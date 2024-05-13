def solution(participant, completion):
    participant.sort()
    completion.sort()
    while True:
        if len(participant) == 1: #두 번 틀림. 1일 경우 예외처리
            return participant[0]
        a = participant.pop()
        b = completion.pop()
        if a != b:
            return a
    return -1