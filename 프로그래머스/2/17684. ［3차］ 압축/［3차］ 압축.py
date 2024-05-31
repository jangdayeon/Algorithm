def solution(msg):
    dic = dict()
    dic_idx = 27
    for i in range(ord('A'), ord('Z')+1):
        dic[chr(i)] = i - ord('A') + 1
    # dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,...}
    
    result = []
    start = 0
    end = 1
    while end <= len(msg):
        while end <= len(msg) and msg[start:end] in dic: #사전에 없는 글자를 찾을 때까지 순회
            end += 1
        result.append(dic[msg[start:end-1]]) #일단 가장 긴 사전에 등록되어있던 글자는 result에 추가해주고
        dic[msg[start:end]] = dic_idx #등록되어 있지 않았던 글자는 추가해주기
        dic_idx += 1 #등록 번호 갱신
        start = end - 1 #다음 글자부터 또 확인
    return result