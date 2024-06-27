#2차원 리스트를 만들어서 [방 넘버, 예약된 시간+10] 으로 데이터 넣게 만들고, li[방 넘버]의 길이는 60*24이다.
import heapq

def solution(book_time):
    book_time.sort(key=lambda x:x[0]) #정렬해서 예약을 시간순으로 받을 수 있게 함
    result = 1
    h = [] #종료시간 넣기
    for book in book_time:
        b0 = list(map(int,book[0].split(':')))
        b1 = list(map(int,book[1].split(':')))
        book_start, book_end = b0[0]*60+b0[1], b1[0]*60+b1[1]+10
        if not h :
            heapq.heappush(h,book_end)
            continue
        if h[0] > book_start:
            result += 1
        else:
            heapq.heappop(h)  
        heapq.heappush(h,book_end)
    return result