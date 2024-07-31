def solution(word):
    dic = {'A':1,'E':2, 'I':3,'O':4, 'U':5}
    result = 0
    for i,w in enumerate(word):
        # print(i,(5**i),(5**(5-i)-1))
        # print((5**i)*(5**(5-i)-1)/4)
        print(dic[w]*(5**(5-i)-1) / 4)
        # print(result)