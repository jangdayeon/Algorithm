def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    for i in range(len(participant)):
        if( i == len(participant)-1):
            return participant[i]
        if(participant[i] != completion[i]):
            return participant[i]
    return ''