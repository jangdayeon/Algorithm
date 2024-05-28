#phone_book의 길이가 백만이므로 1중 for문만으로 코드를 짜야 함
#string으로 정렬하면 앞글자가 같은 것부터 정렬되니깐 그 점을 이용해 나랑 나의 뒷값을 비교했다.
def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True