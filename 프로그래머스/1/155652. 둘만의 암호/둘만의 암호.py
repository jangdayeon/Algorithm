#한 번 틀림. skip에 중복이 없단 말이 없으니깐 set으로 처리 후 계산하도록 해줌
#두 번 틀림. index를 하드코딩했었음^^..
def solution(s, skip, index):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for sk in set(skip):
        alphabet.remove(sk)
    answer = []
    for ss in list(s):
        answer += alphabet[(alphabet.index(ss)+index)%len(alphabet)]
    return ''.join(answer)