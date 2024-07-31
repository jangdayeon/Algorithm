def solution(word):
    dic = {'A':0,'E':1, 'I':2,'O':3, 'U':4}
    result = 0
    for i,w in enumerate(word):
        result += dic[w]*1*(5**(5-i)-1) / 4
    return result + len(word)