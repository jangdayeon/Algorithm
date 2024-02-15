#첫 번째 아이디어
#a,e,i,o,u 각각 5개씩 있는 리스트를 하나 만들고
#이 리스트의 combinations를 구하기
#string으로서 정렬하기
#word는 find 함수로 인덱스 구한 다음 인덱스 +1 리턴하기

from itertools import permutations
def solution(word):
    words = ['A','E','I','O','U']*5
    combi = ['A','E','I','O','U']
    a = set(permutations(words,2))
    a = list(map(list,a))
    a = list(map(lambda x:"".join(x), a))
    combi += a
    a = set(permutations(words,3))
    a = list(map(list,a))
    a = list(map(lambda x:"".join(x), a))
    combi += a
    a = set(permutations(words,4))
    a = list(map(list,a))
    a = list(map(lambda x:"".join(x), a))
    combi += a
    a = set(permutations(words,5))
    a = list(map(list,a))
    a = list(map(lambda x:"".join(x), a))
    combi += a
    combi.sort()
    answer = combi.index(word)
    return answer+1