# fees = [기본 시간, 기본 요금, 단위 시간, 단위 요금]
# records = [시각 차량번호 내역]
#records list 순회
    #IN인 것을 dict에 넣어 데이터를 추가한다.
    #OUT을 발견하면 dict에 내용확인 후 계산해서 result에 넣기, IN에 있는 데이터 삭제
    #dict에 남아있는 데이터는 마지막에 일괄 처리해서 계산 후 result에 넣기
#유의할 점
    # 입출차하고 또 입출차할 수 있음 이걸 전부 계산해야 한다!
    # IN, OUT을 보고 싹 다 계산해서 car_li에 넣은 다음에 시간 계산을 한꺼번에 할 필요가 있다.
    # IN만 했을 경우도 일단 23:59까지 다 구하고 car_li에 값을 +=해주자.
import math
def solution(fees, records):
    car_li = {} #시간 계산해서 넣을 곳
    car_time = {} #총 시간 계산해서 car_li를 정리한 리스트
    #시간 계산해서 car_time 완성하기###################################
    for r in records:
        T, car_num, IO = r.split()
        if IO == "IN":
            car_li[car_num] = T
        else :
            if car_num in car_time:
                car_time[car_num] += timeCalculate(car_li[car_num], T)
            else:
                car_time[car_num] = timeCalculate(car_li[car_num], T)
            del car_li[car_num]
    for c in car_li:
        if c in car_time:
            car_time[c] += timeCalculate(car_li[c], "23:59")
        else:
            car_time[c] = timeCalculate(car_li[c], "23:59")
    #################################################################
    #요금 계산########################################################
    for c in car_time:
        car_time[c] = pay(fees,car_time[c])
    #################################################################
    #정렬#############################################################
    ct_s = sorted(car_time)
    result = []
    for s in ct_s:
        result.append(car_time[s])
    #################################################################
    
    return result

def timeCalculate(start, end): #시간 계산
    s_hour, s_min = start.split(":")
    e_hour, e_min = end.split(":")
    s = int(s_hour)*60+int(s_min)
    e = int(e_hour)*60+int(e_min)
    return e-s

def pay(fees, time): #요금 계산
    if fees[0] >= time : #기본 시간 이내일 경우
        return fees[1]
    else :
        return fees[1] + math.ceil((time-fees[0])/fees[2]) * fees[3]
    