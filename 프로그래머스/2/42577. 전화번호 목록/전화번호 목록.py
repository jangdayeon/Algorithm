#string 정렬은 앞의 글자가 작은 수부터 정렬되므로 이 점을 이용해야 함
#String 정렬과 Int 정렬의 차이점을 꼭 기억할 것

def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(1,len(phone_book)):
        if( phone_book[i][0:len(phone_book[i-1]):] == phone_book[i-1]) :
            return False
        if( i == len(phone_book)-1):
            return True
    return None