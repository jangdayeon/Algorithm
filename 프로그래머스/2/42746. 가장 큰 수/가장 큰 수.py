#str으로 바꿔 정렬해야한다는 건 알았는데, 30이랑 3이랑 비교할 때 어떻게 비교하면 좋을지 생각이 안나 답을 찾아봤다.
#숫자가 30이면 303030, 3이면 333처럼 max_length만큼 반복해서 문자열을 만들어 비교하면 됐다.
#테케 11번만 틀려서 확인했더니 [0,0]일 경우 0을 리턴해야 한다.
def solution(numbers):
    n = list(map(str, numbers))
    max_length = max(map(len, n))
    n = list(map(lambda x:x*max_length, n))
    n.sort(reverse = True)
    n = list(map(lambda x:x[:len(x)//max_length], n))
    result = "".join(n)
    if int(result) == 0 :
        return '0'
    else : 
        return result 