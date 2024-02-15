#participant와 completion을 정렬하고 값이 다른 곳의 값을 리턴 (한 사람 밖에 완주하지 못했다고 했기에)

def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    for i in range(len(participant)):
        if( i == len(participant)-1):
            return participant[i]
        if(participant[i] != completion[i]):
            return participant[i]
    return ''