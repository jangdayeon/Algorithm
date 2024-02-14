def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(1,len(phone_book)):
        if( phone_book[i][0:len(phone_book[i-1]):] == phone_book[i-1]) :
            return False
        if( i == len(phone_book)-1):
            return True
    return None